'''
Created on Apr 18, 2017

@author: jackwang
'''

from __future__ import absolute_import
from celery import chord
from .tasks import add, multiply, tsum
import time, sys
from celery import group, chain, chord, chunks


if __name__ == '__main__':
    
    result = group(add.s(i, i) for i in xrange(10))()
    print 'Group Primitive Task result: ', result.get(timeout=1)
 
    result = chain(add.s(4, 4) | multiply.s(8))()
    print 'Chain Primitive Task result: ', result.get(timeout=1)
 
    result = add.chunks(zip(xrange(100), xrange(100)), 10)()
    print 'Chunks Primitive Task result: ', result.get()

    result = chord( (add.s(i, i) 
                    for i in xrange(2)), tsum.s())()
    print 'Chord Primitive Task result: ', result.get(timeout=1)


