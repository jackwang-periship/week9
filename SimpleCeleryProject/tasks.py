'''
Created on Apr 18, 2017

@author: jackwang
'''
from __future__ import absolute_import
from SimpleCeleryProject.celery import app
import time


@app.task
def longtime_add(x, y):
    print 'long time task begins'
    # sleep 5 seconds
    time.sleep(60)
    print 'long time task finished ZZZZZ'
    return x + y