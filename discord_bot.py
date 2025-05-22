""" Discord bot. """

import logging
import config
import discord
import llm_provider

from typing import cast, TypedDict

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class QueryResponse(TypedDict):
    """ Model for query response. """
    response: str

class BotClient(discord.Client):
    """ Bot handler. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query_engine = None
        self.prompts = None

    async def on_ready(self):
        """ When client is ready handler. """
        user = cast(discord.ClientUser, self.user)
        logging.info("logged on as %s (ID: %s)", user.name, user.id)
        self.query_engine = llm_provider.get_query_engine()
        self.prompts = llm_provider.get_prompts()

    async def on_message(self, message):
        """ When client recieves a message. """
        user = cast(discord.ClientUser, self.user)

        if message.author == user:
            return

        if user.mentioned_in(message):
            # Remove the mention from the message content
            clean_content = message.content.replace(f"<@{user.id}>", "").strip()

            await message.add_reaction("⏳")

            try:
                if self.query_engine and self.prompts:
                    logging.info("processing query from %s: %s", message.author, message.content)

                    # Ask LLM about the user's question.
                    prompt = self.prompts[config.FALLBACK_SYSTEM_PROMPT]
                    question = f"System Prompt: <query_instructions>{prompt}</query_instructions>\n\nUser Question: <user_query>{clean_content}</user_query>"
                    answer = self.query_engine.query(question)

                    # General reply to the server.
                    # await message.channel.send(answer.response)

                    # Replying to that specific message of the person who asked the
                    # question (tagging them as well).
                    # response = cast(str, answer[response)
                    await message.reply(answer.response)
            except Exception as error:
                await message.channel.send("❌ Error generating response")
                logging.error("Error processing query: %s", str(error))
            finally:
                await message.remove_reaction("⏳", self.user)


intents = discord.Intents.default()
intents.message_content = True

client = BotClient(intents=intents)
client.run(config.DISCORD_TOKEN)
