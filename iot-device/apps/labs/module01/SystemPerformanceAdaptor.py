'''
Created on Sep 15, 2018

@author: stannis
'''
import psutil
import threading

from time import sleep

DEFAULT_RATE_IN_SEC=5

class SystemPerformanceAdaptor(threading.Thread):
    enableAdaptor = False
    rateInSec   = DEFAULT_RATE_IN_SEC
    
    def __init__(self,rateInSec = DEFAULT_RATE_IN_SEC):
        super(SystemPerformanceAdaptor,self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
    
    def run(self):
            while True:
                if self.enableAdaptor:
                    print('\n----------------')
                    print('New system performance reading')
                    print('  '+str(psutil.cpu_stats()))
                    print('  '+str(psutil.virtual_memory()))
                    #print('  '+str(psutil.sensors_temperatures(False)))
                    sleep(self.rateInSec)
                