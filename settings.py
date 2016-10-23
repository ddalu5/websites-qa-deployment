import os
from fabric.api import env
from fabric.operations import local

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WEBSITES_DIR = '/var/www/html/tests'
WEBSITE_DB_DIR = '/db'
CONF_FILEPATH = ROOT_DIR+'/websites.yml'

MYSQL_ADMIN_LOGIN = ''
MYSQL_ADMIN_PASSWORD = ''

env.run = local
env.hosts = ['localhost']

try:
    from dev_settings import *
except:
    pass
