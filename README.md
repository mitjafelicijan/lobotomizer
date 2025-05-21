# RAG Chatbot for World of Warcraft with Discord integration

## Installation

```sh
python3 -m venv .venv
source .venv/bin/activate

pip install llama-index llama-index-embeddings-huggingface
```

## Generating vector database

> [!NOTE]
> This repository comes with already generated vector database containing World
> of Warcraft data. But if you add content to corpus you can rerun this again
> and it will create new database.

```sh
source .venv/bin/activate
python gen_storage.py
```
