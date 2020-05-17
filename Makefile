SHELL := /bin/bash
TOP_DIR := $(shell pwd)

test:	build
	cd ${TOP_DIR} && \
	source ${TOP_DIR}/venv/bin/activate && \
	coverage run -m unittest discover --verbose -s . --pattern '*_test.py'

report: test
	source ${TOP_DIR}/venv/bin/activate && \
	coverage xml

python36:
	docker build -f ${TOP_DIR}/Dockerfile.build --build-arg=PYTHON_VERSION=3.6 --tag pygglz-build:3.6 ${TOP_DIR}
	docker run --rm pygglz-build:3.6 make test

python37:
	docker build -f ${TOP_DIR}/Dockerfile.build --build-arg=PYTHON_VERSION=3.7 --tag pygglz-build:3.7 ${TOP_DIR}
	docker run --rm pygglz-build:3.7 make test

python38:
	docker build -f ${TOP_DIR}/Dockerfile.build --build-arg=PYTHON_VERSION=3.8 --tag pygglz-build:3.8 ${TOP_DIR}
	docker run --rm pygglz-build:3.8 make test

all_tests:	test	integration_test

integration_test:	build
	source ${TOP_DIR}/venv/bin/activate && \
	coverage run -m unittest discover --verbose --start-directory ${TOP_DIR}/integration_tests --pattern '*_test.py'

tests:	test

dist:	test
	source ${TOP_DIR}/venv/bin/activate && \
	python3 ${TOP_DIR}/setup.py sdist bdist_wheel

build:	init

init:
	if [ ! -d "${TOP_DIR}/venv/" ]; then \
		virtualenv -p python3 ${TOP_DIR}/venv/; \
	fi && \
	source ${TOP_DIR}/venv/bin/activate && \
	pip install -r ${TOP_DIR}/requirements.txt -r ${TOP_DIR}/requirements-opt.txt -r ${TOP_DIR}/requirements-dev.txt

cleanall:	clean
	cd ${TOP_DIR} && \
	rm -rf venv/

clean:
	cd ${TOP_DIR} && \
	rm -rf .coverage build/ dist/ *.egg-info/

upload:	clean dist
	cd ${TOP_DIR} && \
	source ${TOP_DIR}/venv/bin/activate && \
	twine upload dist/*
