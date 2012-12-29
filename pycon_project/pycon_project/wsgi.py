import os
import sys

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "apps"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pycon_project.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
