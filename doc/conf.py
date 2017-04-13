# -*- coding: utf-8 -*-
import os
import alabaster

# Get the project root dir, which is the parent dir of this
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

# package data
about = {}
with open("../libvcs/__about__.py") as fp:
    exec(fp.read(), about)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'releases',
    'alabaster',
]

releases_unstable_prehistory = True
releases_document_name = "history"
releases_issue_uri = "https://github.com/tony/libvcs/issues/%s"
releases_release_uri = "https://github.com/tony/libvcs/tree/%s"

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = about['__title__']
copyright = about['__copyright__']

version = '%s' % ('.'.join(about['__version__'].split('.'))[:2])
release = '%s' % (about['__version__'])

exclude_patterns = ['_build']

pygments_style = 'sphinx'


html_static_path = ['_static']
html_theme_path = [alabaster.get_path()]
html_favicon = 'favicon.ico'
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'img/libvcs.svg',
}
html_sidebars = {
    '**': [
        'about.html',
        'star.html',
        'navigation.html',
        'relations.html',
        'more.html',
        'searchbox.html',
    ]
}


htmlhelp_basename = '%sdoc' % about['__title__']

latex_documents = [
    ('index', '{0}.tex'.format(about['__package_name__']),
     '{0} Documentation'.format(about['__title__']),
     about['__author__'], 'manual'),
]

man_pages = [
    ('index', about['__package_name__'],
     '{0} Documentation'.format(about['__title__']),
     about['__author__'], 1),
]

texinfo_documents = [
    ('index', '{0}'.format(about['__package_name__']),
     '{0} Documentation'.format(about['__title__']),
     about['__author__'], about['__package_name__'],
     about['__description__'], 'Miscellaneous'),
]

intersphinx_mapping = {
    'py': ('https://docs.python.org/2', None),
    'pip': ('http://sphinx.readthedocs.io/en/latest/', None)
}
