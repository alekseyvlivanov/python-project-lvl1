install:
	poetry install

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

.PHONY: install lint build publish package-install
