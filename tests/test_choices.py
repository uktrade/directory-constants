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
