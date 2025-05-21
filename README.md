# RAG Chatbot for World of Warcraft

This is a easy to use RAG chatbot named after [The
Lobotomizer](https://www.wowhead.com/classic/item=19324/the-lobotomizer) dagger
from World of Warcraft.

- It comes with a WoW specific corpus and pre-generated vector database out of
  this corpus.
- Provides simple and easy to use HTTP API and Discord Bot integration.
- You can use local models via Ollama or external ones like OpenAI, Claude or
  DeepSeek.
- While this is WoW specific, you can easily replace data in `corpus` directory
  with your own and re-run `gen_storage.py` to generate fresh vector database.

## Requirements

- Python 3.10+
- Pip 24.0+
- Lua 5.4+ (only for development)
- GNU Make 4.4+ (only for development)

## Setting up the environment

```sh
git glone git@github.com:mitjafelicijan/lobotomizer.git
cd lobotomizer

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data importing

All the final data that is used in indexing by RAF is located in `corpus`
directory. However this data needs to be first exported from other sources like
pfQuest and other sources like Wowhead comments.

All scripts that generate corpus data are located in `scrapers` directory.

- `warcrafttavern.py` - fetches data from Warcraft Tavern and generates
  markdown files from list of links defined `warcrafttavern.csv`.
- `quests.lua` - takes pfQuest data and generates markdown files of quests.
- `quests-comments.py` - takes `comments.csv` and appends all valid comments to
  quest data. Comment data is provided by web scraper written by
  [kakexd](https://github.com/kakexd/webscrape).

> [!NOTE]
> Do not execute this scripts unnecessarily. These should only be ran after new
> content is being added. Also do not change corpus data.

## Generating vector database

> [!NOTE]
> This repository comes with already generated vector database containing World
> of Warcraft data. But if you add content to corpus you can rerun this again
> and it will create new database.

```sh
source .venv/bin/activate
python gen_storage.py
```

## Corpus data sources

- pfQuest and pfQuest-turtle addon for quests
- wowhead.com for quest comments
- warcrafttavern.com for professions, dungeons, general
- turtle-wow.fandom.com and forum.turtle-wow.org for custom Turtle data
