def pytest_configure():
    from django.conf import settings
    settings.configure()
