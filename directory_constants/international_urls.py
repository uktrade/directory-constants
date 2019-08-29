import functools
from urllib.parse import urljoin
from django.conf import settings

from directory_constants.urls import INTERNATIONAL_CONTACT_TRIAGE


def get_url(url_name, default=None):
    return getattr(settings, url_name, None) or default

HOME = get_url('DIRECTORY_CONSTANTS_URL_GREAT_INTERNATIONAL', 'https://www.great.gov.uk/international/') # noqa
build_url = functools.partial(urljoin, HOME)

# about the UK
ABOUT_UK_INDUSTRIES = build_url('industries/')

# expand
EXPAND_HOME = build_url('expand/')
build_expand_url = functools.partial(urljoin, EXPAND_HOME)
EXPAND_ISD_HOME = build_url('investment-support-directory/')
build_isd_url = functools.partial(urljoin, EXPAND_ISD_HOME)
EXPAND_ISD_SEARCH = build_isd_url('search/')
EXPAND_HOW_TO_SETUP = build_url('how-to-setup-in-the-uk/')
build_how_to_setup_url = functools.partial(urljoin, EXPAND_HOW_TO_SETUP)
EXPAND_HOW_TO_SETUP_VISAS_AND_MIGRATION = build_how_to_setup_url('uk-visas-and-migration/')
EXPAND_HOW_TO_SETUP_TAX_AND_INCENTIVES = build_how_to_setup_url('uk-tax-and-incentives/')
EXPAND_HOW_TO_DO_BUSINESS = build_expand_url('how-to-do-business-with-the-uk/')

# capital invest
CAPITAL_INVEST_HOME = build_url('capital-invest/')

# trade
TRADE_FAS = build_url('trade/')
build_fas_url = functools.partial(urljoin, TRADE_FAS)
TRADE_FAS_SEARCH = build_fas_url('search/')
TRADE_FAS_CONTACT = build_fas_url('contact/')

# about dit
ABOUT_DIT_HOME = build_url('about-dit/')

# news
NEWS = build_url('news/')

# contact
CONTACT = INTERNATIONAL_CONTACT_TRIAGE

# legacy - can be removed once the new site IA has been rolled out.
LEGACY_INVEST = build_url('invest/')