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
    'frontend_dev',
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
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core-specs", "1.3base", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core-specs", "1.3client", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more", "Specs", "package.yml")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "depender", "client", "package.yml")),
)
DEPENDER_SCRIPTS_JSON = []

# Set to true to re-load all JS every time. (slowish)
DEPENDER_DEBUG = True

MOOTOOLS_TEST_LOCATIONS = {
#locations of html tests that should be included in the menu
#these are typically in the Tests directory of the repository
#example: ../more/Tests
  "more": os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more", "Tests")),
}
EXCLUDED_TESTS = [""]

MOOTOOLS_SPECS_AND_BENCHMARKS = ['Core-Specs-1.3client', 'Core-Specs-1.3base', 'More-Tests']

MOOTOOLS_RUNNER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "mootools-runner"))

GENERIC_ASSETS = {
  'Assets.js.test.js': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "Assets.js.test.js")),
  'Assets.css.test.css': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "Assets.css.test.css")),
  'mootools.png': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "mootools.png")),
  'cow.png': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "cow.png")),
  'notExisting.png': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "notExisting.png")),
  'iDontExist.png': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "iDontExist.png")),
  'iDontExistEither.png': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "iDontExistEither.png")),
  'jsonp.js': os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "more", "Specs", "assets", "jsonp.js")),
  
}

MAKO_TEMPLATE_DIRS = (
  os.path.abspath(os.path.join(os.path.dirname(__file__), "frontend_dev", "templates")),
  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "depender", "django", "src", "depender", "templates")),
)

DOC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = {
  "More": os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "more", "Docs")),
  "Core": os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "core", "Docs")),
}

TITLE_PREFIX = 'MooTools Frontend'

BUILDER_PACKAGES = ['Core', 'More']