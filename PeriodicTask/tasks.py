'''
Created on Apr 18, 2017

@author: jackwang
'''
from PeriodicTask.celery import app


@app.task()
def helloworld():
    print "Hello World!"