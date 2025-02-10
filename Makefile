install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

push:
	git add .; git commit -m 'some changes'; git push

lint:
	ruff check gendiff tests

check: 
	test lint

format:
	ruff check gendiff tests --fix

build:
	uv build

.PHONY: install test lint selfcheck check build
