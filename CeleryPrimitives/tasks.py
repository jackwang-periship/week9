'''
Created on Apr 18, 2017

@author: jackwang
'''
from __future__ import absolute_import
from .celery import app
from celery import shared_task
from celery.result import AsyncResult


@shared_task
def add(x, y): 
    return x + y


@shared_task
def multiply(x, y): 
    return x * y


@shared_task
def tsum(numbers): 
    return sum(numbers)


@shared_task
def error_handler(uuid):
    result = AsyncResult(uuid)
    exc = result.get(propagate=False)
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          uuid, exc, result.traceback))
