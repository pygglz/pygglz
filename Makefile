SHELL := /bin/bash
TOP_DIR := ${PWD}

test:	build
	source ${TOP_DIR}/venv/bin/activate && \
	coverage run -m unittest discover --verbose --start-directory ${TOP_DIR}/tests --pattern '*_test.py'

build:	init

init:
	if [ ! -d "${TOP_DIR}/venv/" ]; then \
		virtualenv -p python3.7 ${TOP_DIR}/venv/; \
	fi && \
	source ${TOP_DIR}/venv/bin/activate && \
	pip install -r requirements.txt -r requirements-dev.txt
