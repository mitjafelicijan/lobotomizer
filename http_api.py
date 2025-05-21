""" Testing area. """

import os
import sys
import logging
import config

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

# API key protection for specific routes.

api_key_header = APIKeyHeader(name="x-api-key")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    """ Verifier for API key. """
    if api_key != config.HTTP_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# Make FastAPI application.

app = FastAPI(
    title = config.HTTP_TITLE,
    version = config.HTTP_VERSION,
    description = config.HTTP_DESCRIPTION,
)

# Conditionally enable WebUI (can be enabled/disabled in config.py).

if config.HTTP_ENABLE_WEBUI:
    app.mount("/webui", StaticFiles(directory="webui"), name="webui")

# HTTP validators.

class QueryRequest(BaseModel):
    """ Model for query route. """
    question: str
    prompt: Optional[str] = None
    custom_prompt: Optional[str] = None

    @validator("question")
    def validate_question(cls, v):
        """ Checks if question is passed by. """
        if v is not None:
            if v.strip() == "":
                raise ValueError("Question text must be provided.")
        return v

    @validator("prompt")
    def validate_prompt(cls, v):
        """ Checks if the prompt name actually is loaded. """
        if v is not None:
            if v not in PROMPTS:
                raise ValueError("Prompt name must be a valid one and loaded into server.")
        return v

    @validator("custom_prompt", always=True)
    def validate_custom_prompt(cls, v, values):
        """ Checks if the custom prompt provided has content. """
        if "prompt" not in values or values["prompt"] is None:
            if v.strip() == "":
                raise ValueError("Either prompt or custom_prompt must be provided")
        return v

# Routes.

@app.get("/")
async def default():
    """ Greeting page. """
    return app.openapi()

@app.get("/api/system-prompts", dependencies=[Depends(verify_api_key)])
async def system_prompts():
    """ List all system prompts available. """
    return PROMPTS

@app.post("/api/query", dependencies=[Depends(verify_api_key)])
async def query(req: QueryRequest):
    """ Queries the LLM for the answer. """
    if not QUERY_ENGINE:
        raise HTTPException(status_code=500, detail="Query Engine was not initialized.")

    prompt = req.prompt if req.prompt else req.custom_prompt
    question = f"System Prompt: <query_instructions>{prompt}</query_instructions>\n\nUser Question: <user_query>{req.question}</user_query>"

    return {
        "prompt": req.prompt,
        "custom_prompt": req.custom_prompt,
        "question": req.question,
        "llm_package": question,
        "answer": QUERY_ENGINE.query(question),
        "generated": datetime.now().isoformat(),
    }
