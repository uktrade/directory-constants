build: test_requirements test

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -r requirements_test.txt

flake8:
	flake8 . --exclude=.venv/

pytest:
	pytest . --cov=. --cov-config=.coveragerc $(pytest_args)

test: flake8 pytest

compile_requirements:
	python3 -m piptools compile requirements.ini

compile_test_requirements:
	python3 -m piptools compile requirements_test.ini

compile_all_requirements: compile_requirements compile_test_requirements

.PHONY: build clean test_requirements flake8 pytest test
