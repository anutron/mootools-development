import logging
from os.path import abspath, join, dirname
DOC_ROOT = dirname(__file__)

TITLE_PREFIX = 'MooTools Development'

# Set to true to re-load all JS every time. (slowish)
DEPENDER_DEBUG = True

DEFAULT_VERSION = "1.3"

PROJECTS = {
  "1.2": {
    "Core": {
      "package": "../configurations/1.2/core/package.yml",
      "docs": "../configurations/1.2/core/Docs",
      "build": True
    },
    "More": {
      "package": "../configurations/1.2/more/package.yml",
      "demos": {
        "path": "../configurations/1.2/more/Tests/Interactive",
        "exclude": False
      },
      "docs": "../configurations/1.2/more/Docs",
      "build": True
    }
  },
  "1.3": {
    "Core": {
      "package": "../configurations/1.3/core/package.yml",
      "specs": [
        "../configurations/1.3/core-specs/1.3base/package.yml",
        "../configurations/1.3/core-specs/1.3client/package.yml"
      ],
      "docs": "../configurations/1.3/core/Docs",
      "build": True,
      "fiddles": {
        "path": "../configurations/1.3/fiddles/demos",
        "exclude": False,
        "package": "../configurations/1.3/fiddles/package.yml"
      }
    },
    "More": {
      "package": "../configurations/1.3/more/package.yml",
      "specs": ["../configurations/1.3/more/Tests/Specs/package.yml"],
      "demos": {
        "path": "../configurations/1.3/more/Tests/Interactive",
        "exclude": False
      },
      "docs": "../configurations/1.3/more/Docs",
      "build": True
    }
  }
}

GENERIC_ASSETS = {
  'Assets.js.test.js': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/Assets.js.test.js")),
  'Assets.css.test.css': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/Assets.css.test.css")),
  'mootools.png': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/mootools.png")),
  'cow.png': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/cow.png")),
  'notExisting.png': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/notExisting.png")),
  'iDontExist.png': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/iDontExist.png")),
  'iDontExistEither.png': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/iDontExistEither.png")),
  'jsonp.js': abspath(join(DOC_ROOT, "../configurations/1.3/more/Tests/Specs/assets/jsonp.js")),
}

#############################################################################
###                  DO NOT EDIT BELOW THIS LINE                          ###
#############################################################################


# Django settings for mootools-test-runner project.

logging.basicConfig(level=logging.INFO)

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

MOOTOOLS_RUNNER_PATH = abspath(join(DOC_ROOT, "../mootools-runner"))

MAKO_TEMPLATE_DIRS = (
  abspath(join(DOC_ROOT, "frontend_dev/templates")),
  abspath(join(DOC_ROOT, "../depender/django/src/depender/templates")),
)

DEPENDER_CONFIGURATIONS = {}

for name, project in PROJECTS.iteritems():
  config = DEPENDER_CONFIGURATIONS[name] = {}
  config['DEPENDER_PACKAGE_YMLS'] = []
  config['DEPENDER_SCRIPTS_JSON'] = []
  config['BUILDER_PACKAGES'] = []
  if project.has_key('exclude_blocks') is False:
    config['exclude_blocks'] = []
  for name, repo in project.iteritems():
    if repo.has_key('package'):
      config['DEPENDER_PACKAGE_YMLS'].append(repo['package'])
    if repo.has_key('scripts_json'):
      config['DEPENDER_SCRIPTS_JSON'].append(repo['scripts_json'])
    if repo.has_key('specs'):
      for spec in repo["specs"]:
        config['DEPENDER_PACKAGE_YMLS'].append(spec)
    if repo.has_key('build') and repo["build"] is True:
      config['BUILDER_PACKAGES'].append(name)
    if repo.has_key('fiddles'):
      config['DEPENDER_PACKAGE_YMLS'].append(repo['fiddles']['package'])

def GET_PATH(path):
  return abspath(join(DOC_ROOT, path))
