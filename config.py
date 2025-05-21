""" Configuration for the bot """

# General settings where data is being stored.
CORPUS_DIR = "corpus"
STORAGE_DIR = "storage"
PROMPTS_DIR = "prompts"
HTTP_PORT = 6969

# Uncomment if you want to use local ollama.
PROVIDER = "local_ollama"
EMBEDDINGS = "BAAI/bge-small-en"
OLLAMA_MODEL = "llama3"

# Uncomment if you want to use OpenAI API.
# PROVIDER = "openai"
# API_KEY = ""

# Uncomment if you want to use Claude API.
# PROVIDER = "claude"
# API_KEY = ""
