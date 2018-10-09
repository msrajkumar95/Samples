from Tutorial.settings.base import *

# Override default settings for development
try:
    from Tutorial.settings.local import *
except:
    pass