""" Starts a http server that exposes API to the world. """

import os
import sys
import logging
import config

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from llama_index.core import(
    StorageContext,
    load_index_from_storage,
)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

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
        QUERY_ENGINE = LOCAL_INDEX.as_query_engine(llm=Ollama(model=config.OLLAMA_MODEL, request_timeout=60.0))
    case _:
        logging.error("provide %s doesn't have a handler", config.PROVIDER)
        sys.exit(1)

if not EMBED_MODEL or not LOCAL_INDEX or not QUERY_ENGINE:
    logging.error("starting query engine failed")
    sys.exit(1)

# storage_context = StorageContext.from_defaults(persist_dir=config.STORAGE_DIR)
# local_index = load_index_from_storage(storage_context, embed_model=embed_model)
# query_engine = local_index.as_query_engine(llm=OpenAI(model=OPENAI_MODEL, api_key=OPENAI_APIKEY, request_timeout=60.0))

# question = "What are the best dungeons I can run between levels 30 to 40"
QUESTION = "can i get any good healer priest gear from uldaman"
prompt = f"{QUESTION}\n\n{PROMPTS['general']}"
print(prompt)
response = QUERY_ENGINE.query(prompt)
print(response)
