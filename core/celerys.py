from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    BROKER_URL='redis://localhost:6379/0',  
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',  
)
