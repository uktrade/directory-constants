from directory_constants.constants import urls

import pytest


@pytest.mark.parametrize('url', [
    getattr(urls, attribute_name) for attribute_name in dir(urls)
    if not attribute_name.startswith('__') and attribute_name.isupper()
])
def test_default_links_https(url):
    assert url.startswith('https://')


def test_get_url_value_present(settings):
    settings.DIRECTORY_CONSTANTS_URL_EXPORT_READINESS = 'https://exred.com'

    actual = urls.get_url('DIRECTORY_CONSTANTS_URL_EXPORT_READINESS')

    assert actual == 'https://exred.com'


def test_get_url_value_not_present(settings):
    settings.DIRECTORY_CONSTANTS_URL_EXPORT_READINESS = ''

    actual = urls.get_url('DIRECTORY_CONSTANTS_URL_EXPORT_READINESS')

    assert actual is None


def test_get_url_value_not_default_provided(settings):
    settings.DIRECTORY_CONSTANTS_URL_EXPORT_READINESS = ''

    actual = urls.get_url(
        'DIRECTORY_CONSTANTS_URL_EXPORT_READINESS',
        'www.default.com'
    )

    assert actual == 'www.default.com'


@pytest.mark.parametrize('url_builder,expected', (
    (urls.build_great_url, 'https://www.great.gov.uk/foo/'),
    (urls.build_invest_url, 'https://invest.great.gov.uk/foo/'),
))
def test_url_builders(url_builder, expected):
    assert url_builder('foo/') == expected
    assert url_builder('/foo/') == expected
