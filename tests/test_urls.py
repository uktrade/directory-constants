from directory_constants import urls
from directory_constants.urls import domestic, international, UrlString
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


def test_get_url_value_present(settings):
    settings.TEST_VALUE = 'https://example.com'

    actual = urls.get_url('TEST_VALUE', 'https://other-site.com')

    assert actual == 'https://example.com'


def test_get_url_value_not_present(settings):
    settings.TEST_VALUE = ''

    actual = urls.get_url('TEST_VALUE', 'https://other-site.com')

    assert actual == 'https://other-site.com'


@pytest.mark.parametrize('base,addition', [
    ('https://example.com', 'test'),
    ('https://example.com', 'test/'),
    ('https://example.com', '/test/'),
    ('https://example.com', '/test'),
    ('https://example.com/', 'test'),
    ('https://example.com/', 'test/'),
    ('https://example.com/', '/test/'),
    ('https://example.com/', '/test'),
])
def test_url_string(base, addition):
    base_url = UrlString(base)

    assert base_url / addition == 'https://example.com/test/'
