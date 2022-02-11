from __future__ import absolute_import
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep

logger = get_task_logger(__name__)

@shared_task
def test(duration):
    sleep(duration)
    return 'The test task executed successfully'