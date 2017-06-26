#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jorge J. Riera'
SITENAME = u'mordor-lab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Argentina/Jujuy'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'lazystrap'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
PAGINATED_DIRECT_TEMPLATES = ('archives',)
PAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'))

#All theme text was moved to template variables:

ARCHIVES_TITLE = "Archivos"
COMMENTS_TITLE = "Comentarios"
FEED_TITLE = "RSS"
RECENT_POSTS_TITLE = "Escrituras recientes"
SEARCH_TITLE = "Buscar"
PREV_TITLE = "Previo"
NEXT_TITLE = "Siguiente"
TAG_PAGE_TITLE = "Post tagged by"

#Other theme variables:

SITENAME = "Mordor-lab"
SITESUBTITLE = "Las escrituras del Nigromancer"
SITEKEYWORDS = "GNU Linux Debian Mordor Music Cine Geek Bass"
SITEURL = ""
SOCIAL = (('twitter', 'http://twitter.com/nigrobyte'),)
GITHUB_USERNAME = ""
BLOG_START_YEAR = "2017"
COMMENT_SYSTEM_ID = ""

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [ 'tipue_search']

TEMPLATE_PAGES = {
        'search.html': 'search.html',
        }
