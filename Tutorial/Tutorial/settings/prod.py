from Tutorial.settings.base import *

# Override default settings for development
DEBUG = False

try:
    from Tutorial.settings.local import *
except:
    pass