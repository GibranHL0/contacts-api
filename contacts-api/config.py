"""Creates the configuration for the app."""

import os


class Config(object):
    """Creates the configuration object."""

    raw_uri = os.getenv('DATABASE_URL')
    DATABASE_URI = raw_uri[:8] + 'ql' + raw_uri[8:]
