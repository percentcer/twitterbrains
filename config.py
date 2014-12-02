__author__ = 'spencer'

# dev environment
DEBUG = True

# define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# sqlite database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# application threads, one for
# incoming and one for background work
THREADS_PER_PAGE = 2

# Enable protection against CSRFs
CSRF_ENABLED = True

# Secure key for signing data
CSRF_SESSION_KEY = 'secret'

# Secret key for signing cookies
SECRET_KEY = 'cookie-secret'
