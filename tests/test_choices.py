from operator import itemgetter

from directory_constants import choices, helpers


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


def test_sector_names_structure():
    assert choices.SECTOR_NAMES[0] == ('SL0001', 'Advanced engineering')
    assert len(choices.SECTORS) == 28


def test_sector_names_sorted():
    expected = sorted(choices.SECTOR_NAMES, key=itemgetter(1))
    assert choices.SECTOR_NAMES == expected


def test_sectors_structure():
    assert choices.SECTORS[0] == ('SL10001', 'Advanced Engineering')
    assert len(choices.SECTORS) == 28


def test_sectors_sorted():
    expected = sorted(choices.SECTORS, key=itemgetter(1))
    assert choices.SECTORS == expected


def test_countries_and_territories_structure():
    assert choices.COUNTRIES_AND_TERRITORIES[0] == ('AF', 'Afghanistan')
    country_keys = dict(choices.COUNTRIES_AND_TERRITORIES).keys()
    for uae_territory in helpers.UAE_TERRITORIES_ISO_CODES:
        assert uae_territory not in country_keys
    assert 'AS' in country_keys  # Territory -  American Samoa


def test_countries_and_territories_sorted():
    expected = sorted(choices.COUNTRIES_AND_TERRITORIES, key=itemgetter(1))
    assert choices.COUNTRIES_AND_TERRITORIES == expected


def test_countries_and_territories_removed():
    countries_and_territories = [code for code, _ in choices.COUNTRIES_AND_TERRITORIES]

    assert 'YU' not in countries_and_territories
