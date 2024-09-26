install:
	poetry install

run:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

package-install:
	python3 -m pip install --user dist/*.whl

fool_reinstall:
	poetry build; poetry publish --dry-run;  python3 -m pip install --force-reinstall dist/*.whl
