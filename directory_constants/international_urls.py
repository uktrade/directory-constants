import functools
from directory_constants.urls import get_url, INTERNATIONAL_CONTACT_TRIAGE


def urljoin(base_url, addition):
    stripped_base_url = base_url.strip('/')
    stripped_addition = addition.strip('/')
    return f'{stripped_base_url}/{stripped_addition}/'


HOME = get_url('DIRECTORY_CONSTANTS_URL_GREAT_INTERNATIONAL', 'https://great.gov.uk/international/') # noqa
build_url = functools.partial(urljoin, HOME)
CONTENT_ROOT = build_url('content/')
build_content_url = functools.partial(urljoin, CONTENT_ROOT)

# about the UK
ABOUT_UK_HOME = build_content_url('about-uk/')
build_about_uk_url = functools.partial(urljoin, ABOUT_UK_HOME)
ABOUT_UK_WHY_CHOOSE_UK = build_about_uk_url('why-choose-uk/')
ABOUT_UK_INDUSTRIES = build_content_url('industries/')
ABOUT_UK_REGIONS = build_about_uk_url('regions/')
ABOUT_UK_CONTACT = INTERNATIONAL_CONTACT_TRIAGE

# expand
EXPAND_SLUG = get_url('DIRECTORY_CONSTANTS_EXPAND_SLUG', 'invest/')  # for the transition from invest/ to expand/
EXPAND_HOME = build_url(EXPAND_SLUG)
build_expand_url = functools.partial(urljoin, EXPAND_HOME)
EXPAND_CONTENT_ROOT = build_content_url(EXPAND_SLUG)
build_expand_content_url = functools.partial(urljoin, EXPAND_CONTENT_ROOT)
EXPAND_ISD_HOME = build_url('investment-support-directory/')
build_isd_url = functools.partial(urljoin, EXPAND_ISD_HOME)
EXPAND_ISD_SEARCH = build_isd_url('search/')
EXPAND_HOW_TO_SETUP = build_content_url('how-to-setup-in-the-uk/')
build_how_to_setup_url = functools.partial(urljoin, EXPAND_HOW_TO_SETUP)
EXPAND_HOW_TO_SETUP_VISAS_AND_MIGRATION = build_how_to_setup_url('uk-visas-and-migration/')
EXPAND_HOW_TO_SETUP_TAX_AND_INCENTIVES = build_how_to_setup_url('uk-tax-and-incentives/')
EXPAND_HOW_TO_DO_BUSINESS = build_content_url('how-to-do-business-with-the-uk/')
EXPAND_CONTACT = build_expand_url('contact/')

# capital invest
CAPITAL_INVEST_HOME = build_content_url('capital-invest/')
build_capital_invest_url = functools.partial(urljoin, CAPITAL_INVEST_HOME)
CAPITAL_INVEST_OPPORTUNITIES = build_content_url('opportunities/')
CAPITAL_INVEST_CONTACT = build_capital_invest_url('contact/')

# trade
TRADE_FAS = build_url('trade/')
build_fas_url = functools.partial(urljoin, TRADE_FAS)
TRADE_FAS_SEARCH = build_fas_url('search/')
TRADE_FAS_CONTACT = build_fas_url('contact/')

# about dit
ABOUT_DIT_HOME = build_content_url('about-dit/')
ABOUT_DIT_CONTACT = INTERNATIONAL_CONTACT_TRIAGE

# news
NEWS = build_content_url('news/')

# contact
CONTACT = INTERNATIONAL_CONTACT_TRIAGE
