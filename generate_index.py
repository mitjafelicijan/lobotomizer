""" Generates vector database from corpus. """

import sys
import logging
import config

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

EMBED_MODEL = None

match config.EMBEDDINGS_PROVIDER:
    case "local":
        EMBED_MODEL = HuggingFaceEmbedding(model_name=config.EMBEDDINGS_MODEL)
    case "openai":
        EMBED_MODEL = OpenAIEmbedding(model=config.EMBEDDINGS_MODEL, api_key=config.OPENAI_API_KEY)
    case _:
        logging.error("provider %s doesn't have a handler", config.EMBEDDINGS_PROVIDER)
        sys.exit(1)

if not EMBED_MODEL:
    sys.exit("no embeddings model found")

try:
    documents = SimpleDirectoryReader(input_dir=config.CORPUS_DIR, recursive=True).load_data()
    local_index = VectorStoreIndex.from_documents(documents, embed_model=EMBED_MODEL)
    local_index.storage_context.persist(persist_dir=config.STORAGE_DIR)
    logging.info("building index succeeded")
except Exception as err:
    logging.error("failed building index with %s", err)
