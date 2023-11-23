AUTHOR = 'Olly'
SITENAME = 'Teapot'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'NZ'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ('Pelican', 'https://getpelican.com/'),
    # ('Python.org', 'https://www.python.org/'),
    # ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = {
    'github': 'https://github.com/ollytheninja',
    'linkedin': 'https://linkedin.com/ollytheninja',
}

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/simplify-theme"

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
