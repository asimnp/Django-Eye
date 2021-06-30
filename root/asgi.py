"""
ASGI config for root project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from environs import Env

env = Env()
env.read_env()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env.str('DJANGO_SETTINGS', default='root.settings.production'))

application = get_asgi_application()
