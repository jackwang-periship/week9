'''
Created on Apr 18, 2017

@author: jackwang
'''

from __future__ import absolute_import
from .tasks import add, multiply, tsum
import time, sys
from celery import group


if __name__ == '__main__':
    
    result = group(add.s(i, i) for i in xrange(10)).apply_async()
    print 'Group Primitive Task result: ', result.get(timeout=1)
 
