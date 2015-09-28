## Flask settings.

DEBUG = True

PROJECT_PATH = '/'

STATIC_DIR = r'/static/'

# Maximum allowed size for uploaded content = 16 MB
MAX_CONTENT_LENGTH = 1024 * 1024 * 16;

## User defined settings.

# Directory for uploading files.
UPLOAD_DIR = r'/static/uploads'

from conf_dev import *
