""" Configuration for the bot """

# General settings where data is being stored.
CORPUS_DIR = "corpus"
STORAGE_DIR = "storage"

# Uncomment if you want to use local ollama.
PROVIDER = "local_ollama"
OLLAMA_ENDPOINT = "..."
EMBEDDINGS = "BAAI/bge-small-en"
MODEL = "llama3"

# Uncomment if you want to use OpenAI API.
# PROVIDER = "openai"
# API_KEY = ""

# Uncomment if you want to use Claude API.
# PROVIDER = "claude"
# API_KEY = ""
