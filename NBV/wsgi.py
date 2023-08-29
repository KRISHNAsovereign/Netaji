"""
WSGI config for NBV project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
from whitenoise import WhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NBV.settings')
application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'static'))

# Add any additional directories of static files
application.add_files(os.path.join(os.path.dirname(__file__), 'static'), prefix='static/')

# Set the WSGI application
app = application
