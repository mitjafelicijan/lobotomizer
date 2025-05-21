include makext.mk

help: .help

dev: # Starts development server with reload
	uvicorn http_server:app --port 6969 --workers 1 --reload

server: # Starts production server with max workers
	uvicorn http_server:app --port 6969 --workers $(shell nproc)

index: # Creates vertor database storage
	-rm -rf storage/
	python gen_storage.py
