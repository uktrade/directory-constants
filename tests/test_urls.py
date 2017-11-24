from directory_constants.constants import urls

import pytest


@pytest.mark.parametrize('url', [
    getattr(urls, attribute_name) for attribute_name in dir(urls)
    if not attribute_name.startswith('__')
])
def test_links_https(url):
    assert url.startswith('https://')
