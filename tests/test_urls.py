from directory_constants.urls import domestic, international
import pytest


@pytest.mark.parametrize('url', [
    getattr(domestic, attribute_name) for attribute_name in dir(domestic)
    if not attribute_name.startswith('__') and attribute_name.isupper()
])
def test_domestic_default_links_https(url):
    assert url.startswith('https://')


@pytest.mark.parametrize('url', [
    getattr(international, attribute_name) for attribute_name in dir(international)
    if not attribute_name.startswith('__') and attribute_name.isupper()
])
def test_international_default_links_https(url):
    assert url.startswith('https://')
