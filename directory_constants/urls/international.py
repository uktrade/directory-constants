from directory_constants.urls import UrlString, get_url
from directory_constants.urls.domestic import INTERNATIONAL_CONTACT_TRIAGE

HOME = UrlString(get_url('DIRECTORY_CONSTANTS_URL_GREAT_INTERNATIONAL', 'https://great.gov.uk/international')) # noqa
CONTENT_ROOT = HOME / 'content'

# about the UK
ABOUT_UK_HOME = CONTENT_ROOT / 'about-uk'
ABOUT_UK_WHY_CHOOSE_UK = ABOUT_UK_HOME / 'why-choose-uk'
ABOUT_UK_INDUSTRIES = CONTENT_ROOT / 'industries'
ABOUT_UK_REGIONS = ABOUT_UK_HOME / 'regions'
ABOUT_UK_CONTACT = INTERNATIONAL_CONTACT_TRIAGE

# expand
expand_slug = get_url('DIRECTORY_CONSTANTS_EXPAND_SLUG', 'invest')  # for the transition from invest/ to expand/
EXPAND_HOME = HOME / expand_slug
EXPAND_CONTENT_ROOT = CONTENT_ROOT / expand_slug
EXPAND_ISD_HOME = EXPAND_CONTENT_ROOT / 'investment-support-directory'
EXPAND_ISD_SEARCH = EXPAND_ISD_HOME / 'search'
EXPAND_HOW_TO_SETUP = CONTENT_ROOT / 'how-to-setup-in-the-uk'
EXPAND_HOW_TO_SETUP_VISAS_AND_MIGRATION = EXPAND_HOW_TO_SETUP / 'uk-visas-and-migration'
EXPAND_HOW_TO_SETUP_TAX_AND_INCENTIVES = EXPAND_HOW_TO_SETUP / 'uk-tax-and-incentives'
EXPAND_HOW_TO_DO_BUSINESS = CONTENT_ROOT / 'how-to-do-business-with-the-uk'
EXPAND_CONTACT = EXPAND_HOME / 'contact'

# capital invest
CAPITAL_INVEST_HOME = CONTENT_ROOT / 'capital-invest'
CAPITAL_INVEST_OPPORTUNITIES = CONTENT_ROOT / 'opportunities'
CAPITAL_INVEST_CONTACT = CAPITAL_INVEST_HOME / 'contact'

# trade
TRADE_FAS = HOME / 'trade'
TRADE_FAS_SEARCH = TRADE_FAS / 'search'
TRADE_FAS_CONTACT = TRADE_FAS / 'contact'

# about dit
ABOUT_DIT_HOME = CONTENT_ROOT / 'about-dit'
ABOUT_DIT_CONTACT = INTERNATIONAL_CONTACT_TRIAGE

# news
NEWS = CONTENT_ROOT / 'news/'

# contact
CONTACT = INTERNATIONAL_CONTACT_TRIAGE
