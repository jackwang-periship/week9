'''
Created on Apr 18, 2017

@author: jackwang
'''

from __future__ import absolute_import
from .tasks import add, multiply, tsum
import time, sys
from celery import chord


if __name__ == '__main__':
    
    result = chord((add.s(i, i) for i in xrange(10)), tsum.s()).apply_async()
    print 'Chord Primitive Task result: ', result.get(timeout=60)


