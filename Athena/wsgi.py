"""
WSGI config for Athena project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Athena.settings')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'Athena/static'))
application.add_files(os.path.join(BASE_DIR, 'path/to/more/static/files'), prefix='more-files/')
application.add_files(os.path.join(BASE_DIR, 'media/'), prefix='media/')


