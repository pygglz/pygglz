# [pygglz](https://github.com/cbuschka/pygglz) ![Written in Python](https://img.shields.io/badge/python-3.6%203.7%203.8-blue.svg) [![Build Status](https://travis-ci.org/cbuschka/pygglz.svg?branch=master)](https://travis-ci.org/cbuschka/pygglz) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/cbuschka/pygglz/blob/master/license.txt)

### A feature toggle library designed after Java togglz

## Installation

```bash
pip install pygglz
```

## Usage

```python
from pygglz import features, configure
from pygglz.file_repository import FileRepository

...
configure(state_repository=FileRepository("/home/app/.features.json"))

...

if features["ONE_CLICK_CHECKOUT"]:
  ...
```

## License
Copyright (c) 2020 by [Cornelius Buschka](https://github.com/cbuschka).

[Apache License, Version 2.0](./license.txt)
