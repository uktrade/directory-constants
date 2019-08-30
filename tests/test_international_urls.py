import pytest
from directory_constants import international_urls


@pytest.mark.parametrize('base,addition', (
        ('https://example.com/foo', '/bar'),
        ('https://example.com/foo', '/bar/'),
        ('https://example.com/foo', 'bar'),
        ('https://example.com/foo/', '/bar'),
        ('https://example.com/foo/', '/bar/'),
        ('https://example.com/foo/', 'bar'),
))
def test_urljoin(base, addition):
    assert international_urls.urljoin(base, addition) == 'https://example.com/foo/bar/'


@pytest.mark.parametrize('url_builder,expected', (
    (international_urls.build_url, 'https://great.gov.uk/international/foo/'),
    (international_urls.build_content_url, 'https://great.gov.uk/international/content/foo/'),
    (international_urls.build_about_uk_url, 'https://great.gov.uk/international/content/about-uk/foo/'),
    (international_urls.build_expand_url, 'https://great.gov.uk/international/invest/foo/'),
    (international_urls.build_expand_content_url, 'https://great.gov.uk/international/content/invest/foo/'),
    (international_urls.build_isd_url, 'https://great.gov.uk/international/investment-support-directory/foo/'),
    (international_urls.build_how_to_setup_url, 'https://great.gov.uk/international/content/how-to-setup-in-the-uk/foo/'),  # noqa
    (international_urls.build_capital_invest_url, 'https://great.gov.uk/international/content/capital-invest/foo/'),
    (international_urls.build_fas_url, 'https://great.gov.uk/international/trade/foo/'),
))
def test_url_builders(url_builder, expected):
    assert url_builder('foo/') == expected
    assert url_builder('/foo/') == expected
    assert url_builder('foo') == expected
