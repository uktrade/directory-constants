# directory-constants

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
---

## Installation

```shell
pip install directory-constants
```

## Development

    $ git clone https://github.com/uktrade/directory-constants
    $ cd directory-constants
    [Create and activate your virtual environment]
    $ make test_requirements

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
