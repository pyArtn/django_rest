from celery import Celery
from django.conf import settings

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_practice.settings')
app = Celery('django_rest_practice', broker='redis://localhost')

app.conf.result_backend_transport_options = {
    'retry_policy': {
        'timeout': 5.0
    }
}

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def add(x, y):
    return x + y

