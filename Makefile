install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

push:
	git add .; git commit -m 'some changes'; git push

lint:
	ruff check gendiff tests  # ← Заменили пробелы на табуляцию!

check: test lint

format:
	ruff check gendiff tests --fix  # ← Заменили пробелы на табуляцию!

build:
	uv build

.PHONY: install test lint selfcheck check build
