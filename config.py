import os

class Config(object):
    raw_uri = os.getenv('DATABASE_URL')
    DATABASE_URI = raw_uri[:8] + 'ql' + raw_uri[8:]