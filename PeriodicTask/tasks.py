'''
Created on Apr 18, 2017

@author: jackwang
'''
from celery.decorators import periodic_task
from datetime import timedelta

@periodic_task(run_every=timedelta(seconds=2))
def every_2_seconds():
    print("Running periodic task!")