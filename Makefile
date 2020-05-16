SHELL := /bin/bash
TOP_DIR := ${PWD}

test:	build
	source ${TOP_DIR}/venv/bin/activate && \
	coverage run -m unittest discover --verbose --start-directory ${TOP_DIR}/tests --pattern '*_test.py'

all_tests:	test	integration_test

integration_test:	build
	source ${TOP_DIR}/venv/bin/activate && \
	coverage run -m unittest discover --verbose --start-directory ${TOP_DIR}/integration_tests --pattern '*_test.py'

tests:	test

dist:	test
	source ${TOP_DIR}/venv/bin/activate && \
	python3 ./setup.py sdist bdist_wheel

build:	init

init:
	if [ ! -d "${TOP_DIR}/venv/" ]; then \
		virtualenv -p python3 ${TOP_DIR}/venv/; \
	fi && \
	source ${TOP_DIR}/venv/bin/activate && \
	pip install -r requirements.txt -r requirements-opt.txt -r requirements-dev.txt

cleanall:	clean
	rm -rf venv/

clean:
	rm -rf .coverage build/ dist/ *.egg-info/

upload:	clean dist
	cd ${TOP_DIR} && \
	source ${TOP_DIR}/venv/bin/activate && \
	twine upload dist/*	
