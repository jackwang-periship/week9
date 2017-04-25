'''
Created on Apr 18, 2017

@author: jackwang
'''
from __future__ import absolute_import
from celery import Celery

app = Celery('CeleryPrimitives',
             broker='amqp://jack:avtech@localhost/jack_vhost',
             backend='db+sqlite:///results.sqlite',
             include=['CeleryPrimitives.tasks'])

app.conf.update(
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_RESULT_SERIALIZER = 'json',
    CELERY_ENABLE_UTC = True,
    CELERY_TIMEZONE = 'America/New_York',
    CELERY_TASK_RESULT_EXPIRES=3600,
)

