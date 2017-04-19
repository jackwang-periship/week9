'''
Created on Apr 18, 2017

@author: jackwang
'''
from __future__ import absolute_import

from celery import Celery
from datetime import timedelta

app = Celery('PeriodicTask',
             broker='amqp://jack:avtech@localhost/jack_vhost',
             backend='rpc://',
             include=['PeriodicTask.tasks']
            )

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'add-every-10-seconds': {
        'task': 'PeriodicTask.tasks.helloworld',
        'schedule': timedelta(seconds=10),
        'args': ()
        },
    },
    CELERY_TIMEZONE = 'America/New_York'
)


