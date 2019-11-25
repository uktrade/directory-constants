import pytest

from operator import itemgetter

from directory_constants import choices


def test_country_choices_structure():
    assert choices.COUNTRY_CHOICES[0] == ('AF', 'Afghanistan')


def test_country_choices_sorted():
    expected = sorted(choices.COUNTRY_CHOICES, key=itemgetter(1))
    assert choices.COUNTRY_CHOICES == expected


def test_old_countries_removed():
    country_codes = [code for code, _ in choices.COUNTRY_CHOICES]

    assert 'USSR' not in country_codes
    assert 'GB' in country_codes


def test_sic_codes():
    assert len(choices.SIC_CODES) == 731
    assert choices.SIC_CODES[0] == (
        '69201', 'Accounting and auditing activities'
    )
    assert choices.SIC_CODES[-1] == ('74100', 'specialised design activities')


def test_sectors_structure():
    assert choices.SECTORS[0] == ('SL10001', 'Advanced Engineering')


def test_sectors_sorted():
    expected = sorted(choices.SECTORS, key=itemgetter(1))
    assert choices.SECTORS == expected


def test_countries_and_territories_structure():
    assert choices.COUNTRIES_AND_TERRITORIES[0] == ('AF', 'Afghanistan')
    country_keys = dict(choices.COUNTRIES_AND_TERRITORIES).keys()
    for uae_territory in choices.UAE_TERRITORIES_ISO_CODES:
        assert uae_territory not in country_keys
    assert 'AS' in country_keys  # Territory -  American Samoa


def test_countries_and_territories_sorted():
    expected = sorted(choices.COUNTRIES_AND_TERRITORIES, key=itemgetter(1))
    assert choices.COUNTRIES_AND_TERRITORIES == expected


def test_countries_and_territories_removed():
    countries_and_territories = [code for code, _ in choices.COUNTRIES_AND_TERRITORIES]

    assert 'YU' not in countries_and_territories


def test_countries_and_selected_territories():
    assert choices.COUNTRIES_AND_SELECTED_TERRITORIES[0] == ('AF', 'Afghanistan')
    country_keys = dict(choices.COUNTRIES_AND_SELECTED_TERRITORIES).keys()
    assert choices.HONG_KONG_ISO_CODE in country_keys
    assert 'AS' not in country_keys  # Territory -  American Samoa
    assert choices.UNITED_KINGDOM_ISO_CODE in country_keys


def test_countries_and_selected_territories_sorted():
    expected = sorted(choices.COUNTRIES_AND_SELECTED_TERRITORIES, key=itemgetter(1))
    assert choices.COUNTRIES_AND_SELECTED_TERRITORIES == expected


def test_countries_excluding_gb_and_selected_territories():
    assert choices.COUNTRIES_EXCLUDING_GB_AND_SELECTED_TERRITORIES[0] == ('AF', 'Afghanistan')
    country_keys = dict(choices.COUNTRIES_EXCLUDING_GB_AND_SELECTED_TERRITORIES).keys()
    assert choices.HONG_KONG_ISO_CODE in country_keys
    assert 'AS' not in country_keys  # Territory -  American Samoa
    assert choices.UNITED_KINGDOM_ISO_CODE not in country_keys


def test_countries_excluding_gb_and_selected_territories_sorted():
    expected = sorted(choices.COUNTRIES_EXCLUDING_GB_AND_SELECTED_TERRITORIES, key=itemgetter(1))
    assert choices.COUNTRIES_EXCLUDING_GB_AND_SELECTED_TERRITORIES == expected


def test_filter_country_and_territories_with_empty_list():
    assert choices.filter_country_and_territories([]) == []


@pytest.mark.parametrize(
    'exclude_all_territories,exclude_iso_codes,include_iso_codes,expected_result',
    (
        (
            False,
            [],
            [],
            [
                ('4', 'Four'),
                ('1', 'One'),
                ('3', 'Three'),
                ('2', 'Two'),
            ]
        ),
        (
            False,
            [],
            ['3'],
            [
                ('4', 'Four'),
                ('1', 'One'),
                ('3', 'Three'),
                ('2', 'Two'),
            ]
        ),
        (
            False,
            ['1'],
            [],
            [
                ('4', 'Four'),
                ('3', 'Three'),
                ('2', 'Two'),
            ]
        ),
        (
            True,
            [],
            [],
            [
                ('4', 'Four'),
                ('1', 'One'),
            ]
        ),
        (
            True,
            ['4'],
            [],
            [
                ('1', 'One'),
            ]
        ),
        (
            True,
            ['2'],
            ['2'],
            [
                ('4', 'Four'),
                ('1', 'One'),
            ]
        ),
    )
)
def test_filter_country_and_territories(exclude_all_territories, exclude_iso_codes, include_iso_codes, expected_result):
    countries_and_territories = [
        {'Key': '1', 'Name': 'One', 'Type': 'Country'},
        {'Key': '2', 'Name': 'Two', 'Type': 'Territory'},
        {'Key': '3', 'Name': 'Three', 'Type': 'Territory'},
        {'Key': '4', 'Name': 'Four', 'Type': 'Country'},
    ]
    assert choices.filter_country_and_territories(
        countries_and_territories,
        exclude_all_territories=exclude_all_territories,
        exclude_iso_codes=exclude_iso_codes,
        include_iso_codes=include_iso_codes
    ) == expected_result
