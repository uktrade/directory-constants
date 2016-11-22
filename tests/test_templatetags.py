import pytest

from directory_constants.templatetags import constants_tags


def test_external_url_handles_known_urls():
    for name, url in constants_tags.url_map.items():
        assert constants_tags.external_url(name) == url


def test_external_url_handles_unknown_url():
    with pytest.raises(AssertionError):
        constants_tags.external_url('somewhere')
