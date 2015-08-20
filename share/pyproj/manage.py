#!/usr/bin/env python
# manage.py: A command-line utility that lets you interact with this Django project in various ways. 
# You can read all the details about manage.py in https://docs.djangoproject.com/en/1.8/ref/django-admin/
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
