include makext.mk

help: .help

# Applications and storage

http-api-dev: # Starts development server with reload
	uvicorn http_api:app --port 6969 --workers 1 --reload

http-api: # Starts production server with max workers
	uvicorn http_api:app --port 6969 --workers $(shell nproc)

discord-bot-dev: # Starts development version of Discord bot
	python discord_bot.py

discord-bot: # Starts production version of Discord bot
	python discord_bot.py

index: # Creates vector index database/storage from corpus
	-rm -rf storage/
	python generate_index.py

# General things

provision: # Provisions the machine and installs dependencies
	git lfs install \
		python3 -m venv .venv \
		source .venv/bin/activate \
		pip install -r requirements.txt

# Data importers

lights-hope-extract:
	cd tools/lights_hope && gunzip -k -f world_full_12_november_2020.sql.gz

lights-hope-db: lights-hope-extract # Starts MySQL database and imports Vanilla WoW data into it
	cd tools/ && docker compose -f database.yaml up

extract-quests: # Extracts quest information from pfQuest and add that to corpus
	cd tools/ && lua extract_quests.lua

extract-comments: # Extracts comments from wowhead scrapes and add that to corpus
	cd tools/ && python wowhead_quest_comments.py

fetch-warcrafttavern-pages: # Fetches specific pages from WarcraftTavern and adds them to corpus
	cd tools/ && python warcrafttavern.py

fetch-wowhead-pages: # Fetches specific pages from Wowhead and adds them to corpus
	cd tools/ && python wowhead.py
