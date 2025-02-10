install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build