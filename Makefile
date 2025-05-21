include makext.mk

help: .help

http-api-dev: # Starts development server with reload
	uvicorn http_api:app --port 6969 --workers 1 --reload

http-api: # Starts production server with max workers
	uvicorn http_api:app --port 6969 --workers $(shell nproc)

discord-bot-dev: # Starts a Discord bot
	python discord_bot.py

index: # Creates vertor database storage
	-rm -rf storage/
	python gen_storage.py
