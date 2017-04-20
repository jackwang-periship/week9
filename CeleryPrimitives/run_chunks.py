'''
Created on Apr 18, 2017

@author: jackwang
'''

from __future__ import absolute_import
from .tasks import add, multiply, tsum
import time, sys
from celery import chunks


if __name__ == '__main__':
    
    result = add.chunks(zip(xrange(100), xrange(100)), 10).apply_async()
    print 'Chunks Primitive Task result: ', result.get()


