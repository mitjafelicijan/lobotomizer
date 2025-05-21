""" Generates vector database from corpus. """

import sys
import logging
import config

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

EMBED_MODEL = None

if config.PROVIDER == "local_ollama":
    embed_model = HuggingFaceEmbedding(model_name=config.EMBEDDINGS)

match config.PROVIDER:
    case "local_ollama":
        logging.info("building index using '%s' provider", config.PROVIDER)
        try:
            documents = SimpleDirectoryReader(input_dir=config.CORPUS_DIR, recursive=True).load_data()
            local_index = VectorStoreIndex.from_documents(documents, embed_model=EMBED_MODEL)
            local_index.storage_context.persist(persist_dir=config.STORAGE_DIR)
            logging.info("building index succeeded")
        except Exception as err:
            logging.error("failed building index with %s", err)
    case _:
        logging.error("provider %s doesn't have a handler", config.PROVIDER)
        sys.exit(1)
