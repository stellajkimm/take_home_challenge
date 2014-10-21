"""
WSGI config for take_home_challenge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "take_home_challenge.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# from dj_static import Cling

# application = Cling(get_wsgi_application())

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "take_home_challenge.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()