#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Suvodhoy Sinha'
SITENAME = u'AdMasterMind'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL = (('twitter', 'http://twitter.com/'),
          ('linkedin', 'http://www.linkedin.com/'),
          ('github', 'http://github.com/'),
          ('bitbucket', 'http://bitbucket.com/'),
          ('facebook', 'http://facebook.com/'),
          ('google-plus', 'http://google-plus.com/'))

DEFAULT_PAGINATION = False

STATIC_PATHS = ['theme/static/images',
                'theme/static/fonts',
                'theme/static/css',
                'theme/static/js',
                'extra/CNAME',
                'extra/favicon.ico',
                'extra/robots.txt']

EXTRA_PATH_METADATA = {
    'theme/static/images': {'path': 'images'},
    'theme/static/js': {'path': 'js'},
    'theme/static/fonts': {'path': 'fonts'},
    'theme/static/css': {'path': 'css'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'
THEME_STATIC_DIR = ''


def sidebar_filter(value):
    if value.startswith('archives') or value.startswith('category'):
        return 'right-sidebar'
    elif value == 'index':
        return 'index'
    else:
        return 'no-sidebar'


JINJA_FILTERS = {'sidebar': sidebar_filter}
