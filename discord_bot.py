import os
import sys
import logging
import config
import discord

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from llama_index.core import(
    StorageContext,
    load_index_from_storage,
)

EMBED_MODEL = None
LOCAL_INDEX = None
QUERY_ENGINE = None
PROMPTS = {}

# Loading all the prompts.

for filename in os.listdir(config.PROMPTS_DIR):
    if filename.endswith(".txt"):
        file_path = os.path.join(config.PROMPTS_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            logging.info("loading system prompt from %s", filename)
            name, _ = os.path.splitext(filename)
            PROMPTS[name] = file.read()

# Load vector database from storage.
storage_context = StorageContext.from_defaults(persist_dir=config.STORAGE_DIR)

# Handle query engine.
match config.PROVIDER:
    case "local_ollama":
        logging.info("loading index using '%s' provider", config.PROVIDER)
        EMBED_MODEL = HuggingFaceEmbedding(model_name=config.EMBEDDINGS)
        LOCAL_INDEX = load_index_from_storage(storage_context, embed_model=EMBED_MODEL)
        QUERY_ENGINE = LOCAL_INDEX.as_query_engine(llm=Ollama(
            model = config.OLLAMA_MODEL,
            base_url = config.OLLAMA_BASE_URL,
            request_timeout = 60.0
        ))
    case _:
        logging.error("provide %s doesn't have a handler", config.PROVIDER)
        sys.exit(1)

if not EMBED_MODEL or not LOCAL_INDEX or not QUERY_ENGINE:
    logging.error("starting query engine failed")
    sys.exit(1)


class MyClient(discord.Client):
    async def on_ready(self):
        logging.info("logged on as %s (ID: %s)", self.user.name, self.user.id)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user.mentioned_in(message):
            # Remove the mention from the message content
            clean_content = message.content.replace(f"<@{self.user.id}>", "").strip()

            # Ask LLM about the user's question.
            prompt = PROMPTS[config.FALLBACK_SYSTEM_PROMPT]
            question = f"System Prompt: <query_instructions>{prompt}</query_instructions>\n\nUser Question: <user_query>{clean_content}</user_query>"
            answer = QUERY_ENGINE.query(question)
            logging.info("processing query from %s: %s", message.author, message.content)

            # General reply to the server.
            # await message.channel.send(answer.response)

            # Replying to that specific message of the person who asked the
            # question (tagging them as well).
            await message.reply(answer.response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config.DISCORD_TOKEN)
