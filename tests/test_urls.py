import http

from django.core.urlresolvers import resolve, reverse

from directory_constants.constants import urls

destinations = {
    'about': urls.ABOUT_URL,
    'contact_directory': urls.DIRECTORY_CONTACT_US_URL,
    'contact_sso': urls.SSO_CONTACT_US_URL,
    'events': urls.EVENTS_URL,
    'export_opportunities': urls.EXPORT_OPPORTUNITIES_URL,
    'feedback_directory': urls.DIRECTORY_FEEDBACK_FORM_URL,
    'feedback_sso': urls.SSO_FEEDBACK_FORM_URL,
    'find_a_buyer': urls.FIND_A_BUYER_URL,
    'new_to_exporting': urls.NEW_TO_EXPORTING_URL,
    'occasional_exporter': urls.OCCASIONAL_EXPORTER_URL,
    'privacy': urls.PRIVACY_URL,
    'regular_exporter': urls.REGULAR_EXPORTER_URL,
    'selling_online_overseas': urls.SELLING_ONLINE_OVERSEAS_URL,
    'terms': urls.TERMS_AND_CONDITIONS_URL,
}


def test_redirects(rf):
    for name, expected_url in destinations.items():
        url = reverse(name)
        request = rf.get(url)
        response = resolve(url).func(request)

        assert response.status_code == http.client.FOUND
        assert response.get('Location') == expected_url
