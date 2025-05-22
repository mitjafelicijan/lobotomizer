# RAG Chatbot for World of Warcraft

> [!IMPORTANT]
> This readme still needs work and incomplete.

This is a easy to use RAG chatbot named after [The
Lobotomizer](https://www.wowhead.com/classic/item=19324/the-lobotomizer) dagger
from World of Warcraft.

- It comes with a WoW specific corpus and pre-generated vector database out of
  this corpus.
- Provides simple and easy to use HTTP API and Discord Bot integration.
- You can use local models via Ollama or external ones like OpenAI, Claude or
  DeepSeek.
- While this is WoW specific, you can easily replace data in `corpus` directory
  with your own and re-run `make storage` to generate fresh vector database.

> [!IMPORTANT]
> You can run either HTTP API and/or Discord bot. You do not need to run both
> for the Discord bot to work. They are just two ways of using this RAG system.
> If you just want to use this with Discord you do not need touch HTTP API
> section of this repo.

## Requirements

- Python 3.10+
- Pip 24.0+
- Lua 5.4+ (only for development)
- GNU Make 4.4+ (only for development)
- Git Large File Storage (LFS)

## Setting up the environment

```sh
# Enable large file support.
git lfs install

git glone git@github.com:mitjafelicijan/lobotomizer.git
cd lobotomizer

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Very important!
cp config.example.py config.py

make http-api-dev       # If you want to run HTTP API version of it.
make discord-bot-dev    # If you want to run Discord bot version.
```

## Running HTTP API

```sh
# Make sure your environment is activated.
source .venv/bin/activate

make http-api
```

Then you can open a browser and test it on http://localhost:6969. If you
enabled `HTTP_ENABLE_WEBUI` you can navigate to
http://localhost:6969/webui.chat.html to get a simple web interface to test the
bot.

## Running Discord bot

Before you run the bot you will need to create a Discord Bot Account. Follow
this page [Creating a Bot
Account](https://discordpy.readthedocs.io/en/stable/discord.html). This will
guide you through the process. And after that is done and you obtain `token
key` make sure you update variable `DISCORD_TOKEN` in `config.py` file with the
token you got.

After that you can run the Discord bot with `make discord-bot`.

> [!IMPORTANT]
> Bot will reply only when tagged in a message. This prevents bot for replying
> to all the messages in the channels and basically spamming.

## Data tools

All the final data that is used in indexing by RAF is located in `corpus`
directory. However this data needs to be first exported from other sources like
pfQuest and other sources like Wowhead comments.

Type command `make` from the root of the repository to see all the options.

All scripts that generate corpus data are located in `tools` directory.

- `wct-pages.py` - fetches data from Warcraft Tavern and generates
  markdown files from list of links defined `warcrafttavern.csv`.
- `extract-quests.lua` - takes pfQuest data and generates markdown files of quests.
- `quests-comments.py` - takes `wowhead-quest-comments` and appends all valid
  comments to quest data. Comment data is provided by web scraper written by
  [kakexd](https://github.com/kakexd/webscrape).

> [!NOTE]
> Do not execute this scripts unnecessarily. These should only be ran after new
> content is being added. Also do not change corpus data.

Information about embeddings:

- https://platform.openai.com/docs/guides/embeddings
- https://www.analyticsvidhya.com/blog/2025/03/embedding-for-rag-models/

## Generating vector database

> [!NOTE]
> This repository comes with already generated vector database containing World
> of Warcraft data. But if you add content to corpus you can rerun this again
> and it will create new database.

```sh
source .venv/bin/activate
python gen_storage.py
```

## Deploying to server

This should work on most GNU/Linux distributions. I have tested it on Debian 12.

1. Setup a virtual machine.
2. Create a user with username `lobotomize`.
3. Clone this repository to home directory `/home/lobotomize/` so it ends up
   being `/home/lobotomize/lobotomize/`.
   - `git clone https://github.com/mitjafelicijan/lobotomizer /home/lobotomize/lobotomize`
4. Navigate to repository folder with `cd /home/lobotomize/lobotomize`
5. Make a copy of sample config file `cp config.example.py config.py`
6. Copy systemd service files:
    - `sudo cp *.service /etc/systemd/system/`
7. Enable services and reload systemd:
    - `sudo systemctl daemon-reload`
    - `sudo systemctl enable http_api.service`
    - `sudo systemctl enable discord_bot.service`
    - `sudo systemctl start http_api.service`
    - `sudo systemctl start discord_bot.service`
    - `sudo systemctl status http_api.service`
    - `sudo systemctl status discord_bot.service`
8. Check logs with:
    - `journalctl -u http_api -f`
    - `journalctl -u discord_bot -f`

> [!NOTE]
> Additionally to that you can use Nginx to setup a reverse proxy and add TLS
> with Letsencrypt.

## Corpus data sources

- pfQuest and pfQuest-turtle addon for quests
- wowhead.com for quest comments
- warcrafttavern.com for professions, dungeons, general
- turtle-wow.fandom.com and forum.turtle-wow.org for custom Turtle data

## Reading material

- https://discord.com/privacy/
- https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy
