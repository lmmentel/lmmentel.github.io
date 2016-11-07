# -*- coding: utf-8 -*-

import os

from flask import render_template_string, Markup
from flask_flatpages import pygmented_markdown


def parent_dir(path):
    '''Return the parent of a directory.'''

    return os.path.abspath(os.path.join(path, os.pardir))


def prerender_jinja(text):
    '''A prerender to allow filling jinja2 statements inside markdown'''

    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)


class Configuration(object):

    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True

    # flat pages configuration
    FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
    FLATPAGES_ROOT = os.path.join(APPLICATION_DIR, 'pages')
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_HTML_RENDERER = prerender_jinja

    # freeze configuration

    REPO_NAME = "flask-ghpages-lmmentel"  # Used for FREEZER_BASE_URL

    PROJECT_ROOT = parent_dir(APPLICATION_DIR)

    # In order to deploy to Github pages, you must build the static files to
    # the project root
    FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, 'build')

    # Since this is a repo page (not a Github user page),
    # we need to set the BASE_URL to the correct url as per GH Pages' standards
    FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)

    FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                         # will be deleted when you run the freezer
