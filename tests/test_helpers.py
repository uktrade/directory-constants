from directory_constants.helpers import UrlString, get_url
import pytest


def test_get_url_value_present(settings):
    settings.TEST_VALUE = 'https://example.com'

    actual = get_url('TEST_VALUE', 'https://other-site.com')

    assert actual == 'https://example.com'


def test_get_url_value_not_present(settings):
    settings.TEST_VALUE = ''

    actual = get_url('TEST_VALUE', 'https://other-site.com')

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
