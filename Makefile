.PHONY: installenv help

PATH  := $(PWD)/../venv/bin:$(PWD)/../nodeenv/bin:$(PATH)
SHELL := env PATH=$(PATH) /bin/bash

help: ##how to use
	@echo "installenv help"


installenv: ##install python env and other tools
	@echo "Install Python3 env !"
	@virtualenv -p /usr/bin/python3.6 ../venv
	@pip install -r requirements.txt -i https://pypi.douban.com/simple
	@pip install nodeenv -i https://pypi.douban.com/simple


