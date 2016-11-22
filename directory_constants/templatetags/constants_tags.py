from directory_constants.constants import urls

from django import template

register = template.Library()

urls = {
    "terms": urls.TERMS_AND_CONDITIONS_URL,
    "new_to_exporting": urls.NEW_TO_EXPORTING_URL,
    "feedback_sso": urls.SSO_FEEDBACK_FORM_URL,
    "contact_sso": urls.SSO_CONTACT_US_URL,
    "feedback_directory": urls.DIRECTORY_FEEDBACK_FORM_URL,
    "contact_directory": urls.DIRECTORY_CONTACT_US_URL,
    "events": urls.EVENTS_URL,
    "export_opportunities": urls.EXPORT_OPPORTUNITIES_URL,
    "find_a_buyer": urls.FIND_A_BUYER_URL,
    "occasional_exporter": urls.OCCASIONAL_EXPORTER_URL,
    "regular_exporter": urls.REGULAR_EXPORTER_URL,
    "selling_online_overseas": urls.SELLING_ONLINE_OVERSEAS_URL,
    "about": urls.ABOUT_URL,
    "privacy": urls.PRIVACY_URL,
    "DIT": urls.DIT_URL,
    "exporting_is_great": urls.EXPORTING_IS_GREAT_URL,
}


@register.simple_tag
def external_url(name):
    assert name in urls, 'URL name "{name}"" not found'.format(name=name)
    return urls[name]
