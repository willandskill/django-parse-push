#!/usr/bin/env python

import sys
import django

from django.conf import settings


def main():
    import warnings
    warnings.filterwarnings('error', category=DeprecationWarning)

    if not settings.configured:
        # Dynamically configure the Django settings with the minimum necessary to
        # get Django running tests
        settings.configure(
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.admin',
                'django.contrib.sessions',
                'parse_push',
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                }
            },
            DEBUG=True,
            # ROOT_URLCONF='testproject.urls',
        )

    # Compatibility with Django 1.7's stricter initialization
    if hasattr(django, 'setup'):
        django.setup()

    from django.test.utils import get_runner
    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    if '--failfast' in sys.argv:
        test_runner.failfast = True

    failures = test_runner.run_tests(['parse_push'])

    sys.exit(failures)


if __name__ == '__main__':
    main()