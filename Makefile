install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

lint:
    ruff check gendiff tests

check: test lint

format:
    ruff check gendiff tests --fix
	
build:
	uv build

.PHONY: install test lint selfcheck check build