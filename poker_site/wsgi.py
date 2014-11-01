"""
WSGI config for poker_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/var/www/poker_site/poker_env/BigDeal/poker_site")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
