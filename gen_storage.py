import os
import sys
import logging
import config

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

embed_model = None

if config.PROVIDER == "local_ollama":
    embed_model = HuggingFaceEmbedding(model_name=config.EMBEDDINGS)

if embed_model:
    logging.info(f"building index using '{config.PROVIDER}' model")

    try:
        documents = SimpleDirectoryReader(input_dir=config.CORPUS_DIR, recursive=True).load_data()
        local_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
        local_index.storage_context.persist(persist_dir=config.STORAGE_DIR)
        logging.info(f"building index succeeded")
    except Exception as err:
        logging.info(f"failed building index with {err}")
