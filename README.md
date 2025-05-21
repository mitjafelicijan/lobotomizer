# RAG Chatbot for World of Warcraft

This is a easy to use RAG chatbot named after [The
Lobotomizer](https://www.wowhead.com/classic/item=19324/the-lobotomizer) dagger
from World of Warcraft.

- It comes with a WoW specific corpus and pre-generated vector database out of
  this corpus.
- It provides HTTP API and Discord Bot integration.
- You can use local models via Ollama, OpenAI API, Claude API.
- While this is WoW specific, you can easily replace data in `corpus` directory
  with your own and re-run `gen_storage.py` to generate fresh vector database.

## Installation

```sh
git glone git@github.com:mitjafelicijan/lobotomizer.git
cd lobotomizer

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
