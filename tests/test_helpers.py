import pytest

from directory_constants.helpers import UrlString, get_url, build_country_choices, build_country_region_choices


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


@pytest.mark.parametrize(
    'exclude_all_territories,exclude,include,countries_not_present,countries_present,',
    (
        (
            False,
            [],
            [],
            ['AE-AZ'],
            ['HK', 'GB', 'AS', 'IS'],
        ),
        (
            False,
            ['HK'],
            [],
            ['HK'],
            [],
        ),
        (
            False,
            [],
            ['HK', 'AE-AZ'],
            [],
            ['HK', 'AE-AZ'],
        ),
        (
            False,
            ['HK'],
            ['HK'],
            [],
            ['HK'],
        ),
        (
            True,
            [],
            [],
            ['XXD', 'AS'],
            ['GB', 'IS'],
        ),
        (
            True,
            [],
            ['AS'],
            [],
            ['AS'],
        ),
    )
)
def test_filter_country_and_territories(
    exclude_all_territories,
    exclude,
    include,
    countries_present,
    countries_not_present
):
    actual_countries = build_country_choices(
        exclude_all_territories=exclude_all_territories,
        exclude=exclude,
        include=include,
    )
    country_keys = dict(actual_countries).keys()
    assert len(country_keys) == len(set(country_keys))

    for country in countries_present:
        assert country in country_keys

    for country in countries_not_present:
        assert country not in country_keys


@pytest.mark.parametrize(
    'exclude_all_territories,exclude,include,countries_not_present,countries_present,',
    (
        (
            False,
            [],
            [],
            ['AE-AZ'],
            ['HK', 'GB', 'AS', 'IS'],
        ),
        (
            False,
            ['HK'],
            [],
            ['HK'],
            ['GB', 'IS', 'XXD', 'AS'],
        ),
        (
            True,
            [],
            [],
            ['XXD', 'AS'],
            ['GB', 'IS'],
        ),
    )
)
def test_filter_country_and_territories_regions(
    exclude_all_territories,
    exclude,
    include,
    countries_present,
    countries_not_present
):
    countries_regions = build_country_region_choices(
        exclude_all_territories=exclude_all_territories,
        exclude=exclude,
        include=include,
    )
    total_countries = len(countries_regions)
    print('*****', total_countries)
    country_dict = {}
    for country in countries_regions:
        country_dict[country.get('id')] = country

    for country in countries_present:
        assert country in country_dict

    for country in countries_not_present:
        assert country not in country_dict
