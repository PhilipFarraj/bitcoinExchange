import os

from celery import Celery

import logging

from .settings import API_KEY

LOGGER = logging.getLogger("file")
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bitcoinExchange.settings')

app = Celery('bitcoinExchange')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def hello_world(self):
    from .request import get_data
    get_data("BTC", "USD", API_KEY)
    LOGGER.info("UPDATED DATABASE")
    return str("DONE FIRST")
