from directory_constants import urls
import pytest


@pytest.mark.parametrize('url', [
    getattr(urls.domestic, attribute_name) for attribute_name in dir(urls.domestic)
    if not attribute_name.startswith('__') and attribute_name.isupper()
])
def test_domestic_default_links_https(url):
    assert url.startswith('https://')


@pytest.mark.parametrize('url', [
    getattr(urls.international, attribute_name) for attribute_name in dir(urls.international)
    if not attribute_name.startswith('__') and attribute_name.isupper()
])
def test_international_default_links_https(url):
    assert url.startswith('https://')


@pytest.mark.parametrize('url', [
    getattr(urls.magna, attribute_name) for attribute_name in dir(urls.magna)
    if not attribute_name.startswith('__') and attribute_name.isupper()
])
def test_magna_default_links_https(url):
    assert url.startswith('https://')
