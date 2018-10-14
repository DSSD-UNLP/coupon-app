import django_heroku
import dj_database_url
from couponProject.settings import *

ALLOWED_HOSTS  = ['grupo12-dssd.herokuapp.com']

django_heroku.settings(locals())

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
