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

storage: # Creates vertor database storage from corpus
	-rm -rf storage/
	python gen_storage.py

# Data importers

lights-hope-extract:
	cd tools/lights-hope && gunzip -k -f world_full_12_november_2020.sql.gz

lights-hope-db: lights-hope-extract # Starts MySQL database and imports Vanilla WoW data into it
	cd tools/ && docker compose -f database.yaml up

extract-quests: # Extracts quest information from pfQuest and that to corpus
	cd tools/ && lua extract-quests.lua

fetch-wct-pages: # Fetches specific pages from WCT and adds them to corpus
	cd tools/ && python wct-pages.py
