# directory-constants

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

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

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-constants/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-constants

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-constants/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-constants/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-constants/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-constants

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-constants.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-constants
