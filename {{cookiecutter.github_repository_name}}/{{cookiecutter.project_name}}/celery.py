from __future__ import unicode_literals, absolute_import

from celery import Celery
from django.conf import settings

app = Celery('{{cookiecutter.project_name}}')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
