def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        ROOT_URLCONF='directory_constants.urls',
    )
