""" Configuration for the bot. """

# General settings where data is being stored.
CORPUS_DIR = "corpus"
STORAGE_DIR = "storage"
PROMPTS_DIR = "prompts"

# This prompt will be used if one is not provided.
# Prompts are being read from `prompts` directory and the basename of the file
# is used as a value for this variable.
FALLBACK_SYSTEM_PROMPT = "general"

# HTTP server stuff.
# IMPORTANT: Change this API Key!!! This is just for example!
HTTP_API_KEY = "CY75rERBdRneQUXpJmOYmF6228enSqMqHZRD5kRjhFhhUGnBtwfFL8ELgX1jw1Lv"
HTTP_PORT = 6969
HTTP_TITLE = "Lobotomizer"
HTTP_VERSION = "1.0alpha"
HTTP_DESCRIPTION = "WoW Chatbot"
HTTP_ENABLE_WEBUI = True

# Below are available provider. ONLY one can be used at the time!
# Uncomment which one you need and comment out the rest of them.

# Uncomment if you want to use local models with Ollama.
PROVIDER = "local_ollama"
EMBEDDINGS = "BAAI/bge-small-en"
OLLAMA_MODEL = "llama3"

# Uncomment if you want to use OpenAI API.
# PROVIDER = "openai"
# API_KEY = ""

# Uncomment if you want to use DeepSeek API.
# PROVIDER = "deepseek"
# API_KEY = ""

# Uncomment if you want to use Claude API.
# PROVIDER = "claude"
# API_KEY = ""
