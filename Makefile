SHELL := /bin/bash
PROJECT_DIR ?= $(shell git rev-parse --show-toplevel)


.PHONY: install-dev
install-dev:
	poetry env use 3.11
	poetry install --with dev


.PHONY: activate-env
activate-env:
	poetry shell


.PHONY: format
format:
	poetry run ruff format $(PROJECT_DIR)/src/


.PHONY: lint
lint:
	poetry run ruff check $(PROJECT_DIR)/src/
	poetry run mypy $(PROJECT_DIR)/src/


.PHONY: start-dev-server
start-dev-server:
	PYTHONPATH=$(PROJECT_DIR)/src/ uvicorn src.be.app:app --host 127.0.0.1 --port 8000 --reload
