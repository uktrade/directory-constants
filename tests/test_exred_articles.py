from directory_constants.constants import exred_articles


def test_exred_articles_unique():
    # https://stackoverflow.com/a/9759842/904887
    article_uuids = [
        getattr(exred_articles, variable_name)
        for variable_name in dir(exred_articles)
        if not variable_name.startswith("__")
    ]
    assert len(set(article_uuids)) == len(article_uuids)
