""" Configuration for the bot. """

# General settings where data is being stored.
CORPUS_DIR = "corpus"
STORAGE_DIR = "storage"
PROMPTS_DIR = "prompts"

# This prompt will be used if one is not provided.
# Prompts are being read from `prompts` directory and the basename of the file
# is used as a value for this variable.
FALLBACK_SYSTEM_PROMPT = "general"

# Discord stuff.
DISCORD_TOKEN = ""

# HTTP server stuff.
HTTP_API_KEY = ""
HTTP_PORT = 6969
HTTP_TITLE = "Lobotomizer"
HTTP_VERSION = "1.0alpha"
HTTP_DESCRIPTION = "WoW Chatbot"
HTTP_ENABLE_WEBUI = True

# Which model should be used for creating embeddings.
# Note: Use remote ones if you don't have a good GPU on your machine.
#  PROVIDER   MODEL                             COMMENT
#  local      BAAI/bge-small-en                 small and relatively ok
#  local      intfloat/e5-mistral-7b-instruct   excellent but GPU intensive
#  local      NovaSearch/stella_en_1.5B_v5      excellent but GPU intensive
#  openai     text-embedding-3-small
#  openai     text-embedding-3-large
EMBEDDINGS_PROVIDER = "openai"
EMBEDDINGS_MODEL = "text-embedding-3-small"

# Below are available provider. ONLY one can be used at the time!
# Provider options: ollama, openai, deepseek, anthropic
LLM_PROVIDER = "openai"

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3"

OPENAI_API_KEY = ""
OPENAI_MODEL = "gpt-4o-mini"

DEEPSEEK_API_KEY = ""
DEEPSEEK_MODEL = "deepseek-chat"

ANTHROIPIC_API_KEY = ""
ANTHROIPIC_MODEL = "claude-3-7-sonnet-latest"
