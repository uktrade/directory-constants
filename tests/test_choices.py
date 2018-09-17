from operator import itemgetter

from directory_constants.constants import choices


def test_country_choices_structure():
    assert choices.COUNTRY_CHOICES[0] == ('AF', 'Afghanistan')


def test_country_choices_sorted():
    expected = sorted(choices.COUNTRY_CHOICES, key=itemgetter(1))
    assert choices.COUNTRY_CHOICES == expected
