'''
Created on Sep 15, 2018

@author: stannis
'''
from labs.common import SensorData
from labs.module02 import SmtpClientConnector
from cgitb import enable
from labs.module01.SystemPerformanceAdaptor import DEFAULT_RATE_IN_SEC
from random import random
from random import uniform
from builtins import str
from asyncio.tasks import sleep
from test.test_enum import threading

Sens = SensorData.SensorData()
SmtpClientConnector = SmtpClientConnector.SmtpClientConnector()


class TempSensorEmulator(threading.Thread):
    enableEmulator = False
    isPrevTempSet = False
    rateInSec = DEFAULT_RATE_IN_SEC
    
    Sens.setName('Temperature')
    
    lowVal = 5
    highVal = 30
    alertDiff = 5
    
    def __init__(self, rateInSec = DEFAULT_RATE_IN_SEC):
        super(TempSensorEmulator, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        
 


    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = uniform(float(self.lowVal), float(self.highVal))
                Sens.addValue(self.curTemp)
                
                print('\n------------')
                print('New sensor reading:')
                print(' ' + str(self.curTemp))
                
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp
                    self.isPrevTempSet = True
                
                else:
                    print(Sens.__str__())
                    print('inCurTemp - AvgValue =' + str(abs(self.curTemp - Sens.getAvgValue())))
                    print('Threshold =' + str(self.alertDiff))
                    
                    if (abs(self.curTemp - Sens.getAvgValue()) >= self.alertDiff):
                        print('inCurrent temp exceeds average by >' + str(self.alertDiff) + 'TriggeringAlert...')
                        self.sensorData = Sens.__str__()
                        SmtpClientConnector.publishMessage('Exceptional Sensor Data [test]', self.sensorData) 
                    sleep(self.rateInSec)
                    
                
        
        