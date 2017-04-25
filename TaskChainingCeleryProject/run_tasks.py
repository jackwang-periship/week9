'''
Created on Apr 18, 2017

@author: jackwang
'''
from .tasks import update_page_info
import time, sys

if __name__ == '__main__':
    
    zipcode = ' '.join(sys.argv[1:]) or "07436"
    
    result = update_page_info.delay(zipcode)
    # at this time, our task is not finished, so it will return False
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
    # sleep 10 seconds to ensure the task has been finished
    while True:
        time.sleep(5)
        # now the task should be finished and ready method will return True
        print 'Task finished? ', result.ready()
        print 'Task result: ', result.result
        if result.ready() is True:
            break
        
    