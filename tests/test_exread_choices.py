from directory_constants.constants import choices, exred_articles


def test_all_exread_articles_are_in_choices():
    # It's a bit hacky but it needs to be programmatic
    article_uuids = [
        getattr(exred_articles, variable_name)
        for variable_name in dir(exred_articles)
        if not variable_name.startswith("__")
    ]
    assert len(article_uuids) == len(choices.EXREAD_ARTICLES_CHOICES)
