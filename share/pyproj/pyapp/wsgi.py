"""
WSGI config for pyapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/

wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. 
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyapp.settings")

application = get_wsgi_application()
