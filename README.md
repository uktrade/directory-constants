# directory-constants

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![snyk-image]][snyk]

---

## Requirements

```shell
pip install -r requirements.txt
```

## Installation

```shell
pip install -e git+https://git@github.com/uktrade/directory-constants.git@0.0.1#egg=directory-constants
```

## Usage

```python
# urls.py
from directory_constants import urls as external_urls

url_patterns = urls.url_patterns + [
   ...
]
```

## Development

    $ git clone https://github.com/uktrade/directory-constants
    $ cd directory-constants

## Testing
	$ make test

## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIRECTORY_PYPI_USERNAME     |
| DIRECTORY_PYPI_PASSWORD     |


Then run the following command:

    make publish


[circle-ci-image]: https://circleci.com/gh/uktrade/directory-constants/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-constants/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-constants/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-constants

[pypi-image]: https://badge.fury.io/py/directory-constants.svg
[pypi]: https://badge.fury.io/py/directory-constants

[snyk-image]: https://snyk.io/test/github/uktrade/directory-constants/badge.svg
[snyk]: https://snyk.io/test/github/uktrade/directory-constants
