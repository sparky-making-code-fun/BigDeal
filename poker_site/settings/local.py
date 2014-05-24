from base import *

# For your own local private settings
# Those should go into local_settings.py
# and then set your DJANGO_SETTINGS_MODULE to poker_site.settings.local
try:
    from local_settings import *
except:
    pass
