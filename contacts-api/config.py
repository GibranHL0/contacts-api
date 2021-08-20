"""Creates the configuration for the app."""

import os


class Config(object):
    """Creates the configuration object."""

    raw_uri = os.getenv('DATABASE_URL')
    raw_uri = 'postgres://yyomyofxhndwkx:42c05705f098442101fa4f9a3490a71ad72d26dfd784063972a1ee49a2f2b675@ec2-18-215-111-67.compute-1.amazonaws.com:5432/d24nk8chisovpo'
    DATABASE_URI = raw_uri[:8] + 'ql' + raw_uri[8:]
