""" Returns back LLM Query engine based on the configuration. """

import os
import sys
import config
import logging
import typing

from llama_index.core.query_engine import BaseQueryEngine

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from llama_index.llms.deepseek import DeepSeek
from llama_index.llms.anthropic import Anthropic

from llama_index.core import(
    StorageContext,
    load_index_from_storage,
)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def get_prompts() -> dict[str, str]:
    """ Reads andreturns system prompts from prompts directory. """
    prompts = {}
    for filename in os.listdir(config.PROMPTS_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(config.PROMPTS_DIR, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                logging.info("loading system prompt from %s", filename)
                name, _ = os.path.splitext(filename)
                prompts[name] = file.read()
    return prompts

def get_embeddings_model():
    """ Returns the model used to create embeddings. """
    embed_model = None

    match config.EMBEDDINGS_PROVIDER:
        case "local":
            embed_model = HuggingFaceEmbedding(model_name=config.EMBEDDINGS_MODEL)
        case "openai":
            embed_model = OpenAIEmbedding(model=config.EMBEDDINGS_MODEL, api_key=config.OPENAI_API_KEY)
        case _:
            logging.error("provider %s doesn't have a handler", config.EMBEDDINGS_PROVIDER)

    return embed_model

def get_query_engine() -> typing.Optional[BaseQueryEngine]:
    """ Returns back the appropriate query engine. """
    query_engine = None

    # Load vector database from storage.
    embed_model = get_embeddings_model()
    storage_context = StorageContext.from_defaults(persist_dir=config.STORAGE_DIR)
    local_index = load_index_from_storage(storage_context, embed_model=embed_model)

    logging.info("loading index using '%s' provider", config.LLM_PROVIDER)

    # Handle query engine.
    match config.LLM_PROVIDER:
        case "ollama":
            query_engine = local_index.as_query_engine(
                streaming = False,
                llm = Ollama(
                    model = config.OLLAMA_MODEL,
                    base_url = config.OLLAMA_BASE_URL,
                    request_timeout = 60.0))
        case "openai":
            query_engine = local_index.as_query_engine(
                    streaming = False,
                    llm = OpenAI(
                        model = config.OPENAI_MODEL,
                        api_key = config.OPENAI_API_KEY,
                        request_timeout = 60.0))
        case "deepseek":
            query_engine = local_index.as_query_engine(
                    streaming = False,
                    llm = DeepSeek(
                        model = config.DEEPSEEK_MODEL,
                        api_key = config.DEEPSEEK_API_KEY,
                        request_timeout = 60.0))
        case "anthropic":
            query_engine = local_index.as_query_engine(
                    streaming = False,
                    llm = Anthropic(
                        model = config.ANTHROIPIC_MODEL,
                        api_key = config.ANTHROIPIC_API_KEY,
                        request_timeout = 60.0))
        case _:
            logging.error("provide %s doesn't have a handler", config.LLM_PROVIDER)
            sys.exit(1)

    if not embed_model or not local_index or not query_engine:
        logging.error("starting query engine failed")

    return query_engine
