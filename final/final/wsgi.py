"""
WSGI config for final project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
>>>>>>> 83b18517b996126d929708f41d44fccf92ba3ade
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

application = get_wsgi_application()
