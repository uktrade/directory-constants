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
	python3 -m piptools compile requirements.in

compile_test_requirements:
	python3 -m piptools compile requirements_test.in

compile_all_requirements: compile_requirements compile_test_requirements

makemessages:
	django-admin makemessages \
		--locale ar \
		--locale de \
		--locale en_GB \
		--locale es \
		--locale fr \
		--locale ja \
		--locale pt \
		--locale pt_BR \
		--locale zh_Hans \
		--no-wrap

compilemessages:
	django-admin compilemessages

publish:
	rm -rf build dist; \
	python setup.py bdist_wheel; \
	twine upload --username $$DIRECTORY_PYPI_USERNAME --password $$DIRECTORY_PYPI_PASSWORD dist/*

.PHONY: build clean test_requirements flake8 pytest test publish
