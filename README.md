# directory-constants

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![semver-image]][semver]

---

## Installation

```shell
pip install directory-constants
```

### Environment variables

To change the default value of urls add the following to your settings.py:

| Setting name                                    | default value                                         |
| ----------------------------------------------- | ----------------------------------------------------- |
| DIRECTORY_CONSTANTS_URL_GREAT_DOMESTIC          | https://www.great.gov.uk                              |
| DIRECTORY_CONSTANTS_URL_SINGLE_SIGN_ON          | https://www.great.gov.uk/sso/                         |
| DIRECTORY_CONSTANTS_URL_EXPORT_OPPORTUNITIES    | https://www.great.gov.uk/export-opportunities/        |
| DIRECTORY_CONSTANTS_URL_FIND_A_BUYER            | https://www.great.gov.uk/find-a-buyer/                |
| DIRECTORY_CONSTANTS_URL_SELLING_ONLINE_OVERSEAS | https://www.great.gov.uk/selling-online-overseas/     |
| DIRECTORY_CONSTANTS_URL_FIND_A_SUPPLIER         | https://www.great.gov.uk/trade/                      |
| DIRECTORY_CONSTANTS_URL_INVEST                  | https://invest.great.gov.uk                           |
| DIRECTORY_CONSTANTS_URL_EVENTS                  | https://www.events.trade.gov.uk                       |


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

[semver-image]: https://img.shields.io/badge/Versioning%20strategy-SemVer-5FBB1C.svg
[semver]: https://semver.org
