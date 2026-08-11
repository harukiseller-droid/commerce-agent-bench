.PHONY: install test eval check

install:
	python -m pip install -e . pytest

test:
	pytest -q

eval:
	python scripts/run_evals.py

check: test eval
