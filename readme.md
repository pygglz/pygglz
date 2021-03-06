# [pygglz](https://github.com/pygglz/pygglz) ![Written in Python](https://img.shields.io/badge/python-3.6,%203.7,%203.8-blue.svg) [![PyPI](https://img.shields.io/pypi/v/pygglz)](https://pypi.org/project/pygglz/) [![Build Status](https://travis-ci.com/pygglz/pygglz.svg?branch=master)](https://travis-ci.com/pygglz/pygglz) [![codecov](https://codecov.io/gh/pygglz/pygglz/branch/master/graph/badge.svg)](https://codecov.io/gh/pygglz/pygglz) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/pygglz/pygglz/blob/master/license.txt)

### A feature toggle library designed after Java togglz

## Features
* Global and thread local feature contexts
* Feature state snapshots

### Storages for feature state
* File storage (json)
* DynamoDB table
* HTTP service

## Installation

```bash
pip install pygglz
```

## Usage

### Features from local JSON file

```python
from pygglz import features
from pygglz.file import FileRepository

...
pygglz.configure(state_repository=FileRepository("/home/app/.features.json"))

...

if features["ONE_CLICK_CHECKOUT"]:
  ...
```

### Features from DynamoDB table "features"

```python
from pygglz import features
from pygglz.dynamodb import DynamodbRepository

...
pygglz.configure(state_repository=DynamodbRepository())

...

if features["ONE_CLICK_CHECKOUT"]:
  ...
```

## License
Copyright (c) 2020 by [Cornelius Buschka](https://github.com/cbuschka).

[Apache License, Version 2.0](./license.txt)
