import logging
from os.path import abspath, join, dirname, normpath
DOC_ROOT = dirname(__file__)
ROOT = abspath(join(DOC_ROOT, '../../'))

TITLE_PREFIX = 'MooTools Development'

# Set to true to re-load all JS every time. (slowish)
DEPENDER_DEBUG = True

DEFAULT_VERSION = "MooTools Edge"


PROJECTS = {
  "MooTools Edge": {
    "Core": {
      "package": "lib/core-edge/package.yml",
      "build": True,
      "docs": "lib/core-edge/",
      "specs": ["lib/core-edge/Specs/1.2/package.yml",
                "lib/core-edge/Specs/1.3base/package.yml",
                "lib/core-edge/Specs/1.3client/package.yml",
                "lib/core-edge/Specs/1.4base/package.yml",
                "lib/core-edge/Specs/1.4client/package.yml",
                "lib/core-edge/Specs/1.5base/package.yml",
                "lib/core-edge/Specs/1.5client/package.yml"]
    },
    "More": {
      "package": "lib/more-edge/package.yml",
      "build": True,
      "demos": {
        "path": "lib/more-edge/Tests/Interactive"
      },
      "specs": ["lib/more-edge/Tests/Specs/package.yml"],
      "docs": "lib/more-edge/"
    }
  }
}

GENERIC_ASSETS = {
  'Assets.js.test.js': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/Assets.js.test.js")),
  'Assets.css.test.css': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/Assets.css.test.css")),
  'mootools.png': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/mootools.png")),
  'cow.png': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/cow.png")),
  'notExisting.png': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/notExisting.png")),
  'iDontExist.png': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/iDontExist.png")),
  'iDontExistEither.png': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/iDontExistEither.png")),
  'jsonp.js': abspath(join(ROOT, "lib/more-edge/Tests/Specs/assets/jsonp.js")),
}

#############################################################################
###                  DO NOT EDIT BELOW THIS LINE                          ###
#############################################################################


def PATH_FROM_ROOT(path):
  return normpath('../../' + path)

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
    if repo.has_key('docs'):
      repo['docs'] = PATH_FROM_ROOT(repo['docs'])
    if repo.has_key('demos'):
      repo['demos']['path'] = PATH_FROM_ROOT(repo['demos']['path'])
      if repo['demos'].has_key('assets'):
        repo['demos']['assets'] = PATH_FROM_ROOT(repo['demos']['assets'])
    if repo.has_key('package'):
      repo['package'] = PATH_FROM_ROOT(repo['package'])
      config['DEPENDER_PACKAGE_YMLS'].append(repo['package'])
    if repo.has_key('scripts_json'):
      repo['scripts_json'] = PATH_FROM_ROOT(repo['scripts_json'])
      config['DEPENDER_SCRIPTS_JSON'].append((name, repo['scripts_json']))
    if repo.has_key('specs'):
      specs = []
      for spec in repo["specs"]:
        spec = PATH_FROM_ROOT(spec)
        specs.append(spec)
        config['DEPENDER_PACKAGE_YMLS'].append(spec)
      repo['specs'] = specs
    if repo.has_key('build') and repo["build"] is True:
      config['BUILDER_PACKAGES'].append(name)
    if repo.has_key('fiddles'):
      repo['fiddles']['package'] = PATH_FROM_ROOT(repo['fiddles']['package'])
      repo['fiddles']['path'] = PATH_FROM_ROOT(repo['fiddles']['path'])
      config['DEPENDER_PACKAGE_YMLS'].append(repo['fiddles']['package'])

def GET_PATH(path):
  return abspath(join(DOC_ROOT, path))
