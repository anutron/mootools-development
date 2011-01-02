# Django settings for mootools-test-runner project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'djangomako.middleware.MakoMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'test_runner',
    'depender',
    'django_extensions',
    'django.contrib.markup',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
)

import os
import logging
logging.basicConfig(level=logging.INFO)

DEPENDER_PACKAGE_YMLS = (
#locations of all your package yamls
#in this example, they're all located in the directory above the test runner
#for example, ../core/package.yml for core
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "behavior", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more-behaviors", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "depender", "client", "package.yml")),
)
DEPENDER_SCRIPTS_JSON = []

# Set to true to re-load all JS every time. (slowish)
DEPENDER_DEBUG = True

MOOTOOLS_TEST_LOCATIONS = {
#locations of html tests that should be included in the menu
#these are typically in the Tests directory of the repository
#example: ../more/Tests

  "more-behaviors": os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more-behaviors", "Tests")),
  "behavior": os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "behavior", "Tests")),
  "more": os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more", "Tests")),
}

EXCLUDED_TESTS = ["more"]

MAKO_TEMPLATE_DIRS = (
  os.path.abspath(os.path.join(os.path.dirname(__file__), "test_runner", "templates")),
)

TITLE_PREFIX = 'MooTools Tests'