'''
Created on Apr 18, 2017

@author: jackwang
'''

from __future__ import absolute_import
from .tasks import add, multiply, tsum
import time, sys
from celery import chain


if __name__ == '__main__':
    
    result = chain(add.s(4, 4) | multiply.s(8)).apply_async()
    print 'Chain Primitive Task result: ', result.get(timeout=1)
 
