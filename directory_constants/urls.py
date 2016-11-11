from django.conf.urls import url
from django.views.generic import RedirectView

from directory_constants.constants import urls


urlpatterns = [
    url(r"^terms_and_conditions$",
        RedirectView.as_view(url=urls.TERMS_AND_CONDITIONS_URL),
        name="terms"),

    url(r"^new_to_exporting$",
        RedirectView.as_view(url=urls.NEW_TO_EXPORTING_URL),
        name="new_to_exporting"),

    url(r"^feedback_sso$",
        RedirectView.as_view(url=urls.SSO_FEEDBACK_FORM_URL),
        name="feedback_sso"),

    url(r"^contact_sso$",
        RedirectView.as_view(url=urls.SSO_CONTACT_US_URL),
        name="contact_sso"),

    url(r"^feedback_directory$",
        RedirectView.as_view(url=urls.DIRECTORY_FEEDBACK_FORM_URL),
        name="feedback_directory"),

    url(r"^contact_directory$",
        RedirectView.as_view(url=urls.DIRECTORY_CONTACT_US_URL),
        name="contact_directory"),

    url(r"^events$",
        RedirectView.as_view(url=urls.EVENTS_URL),
        name="events"),

    url(r"^export_opportunities$",
        RedirectView.as_view(url=urls.EXPORT_OPPORTUNITIES_URL),
        name="export_opportunities"),

    url(r"^find_a_buyer$",
        RedirectView.as_view(url=urls.FIND_A_BUYER_URL),
        name="find_a_buyer"),

    url(r"^occasional_exporter$",
        RedirectView.as_view(url=urls.OCCASIONAL_EXPORTER_URL),
        name="occasional_exporter"),

    url(r"^regular_exporter$",
        RedirectView.as_view(url=urls.REGULAR_EXPORTER_URL),
        name="regular_exporter"),

    url(r"^selling_online_overseas$",
        RedirectView.as_view(url=urls.SELLING_ONLINE_OVERSEAS_URL),
        name="selling_online_overseas"),

    url(r"^about$",
        RedirectView.as_view(url=urls.ABOUT_URL),
        name="about"),

    url(r"^privacy$",
        RedirectView.as_view(url=urls.PRIVACY_URL),
        name="privacy"),

    url(r"^DIT$",
        RedirectView.as_view(url=urls.DIT_URL),
        name="DIT"),

]
