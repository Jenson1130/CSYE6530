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

SenDat = SensorData.SensorData()
SmtpClientConnector = SmtpClientConnector.SmtpClientConnector()


class TempSensorEmulator(threading.Thread):
    enableEmulator = False
    PrevTempS = False
    rateInSec = DEFAULT_RATE_IN_SEC
    
    SenDat.setName('Temperature')
    
    lowVal = 5
    highVal = 30
    alertDiff = 1
    
    def __init__(self, rateInSec = DEFAULT_RATE_IN_SEC):
        super(TempSensorEmulator, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        
 


    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = uniform(float(self.lowVal), float(self.highVal))
                SenDat.addValue(self.curTemp)
                
                print('\n------------')
                print('Sensor reading:')
                print(' ' + str(self.curTemp))
                
                if self.PrevTempSet == False:
                    self.prevTempS = self.curTemp
                    self.PrevTempS = True
                
                else:
                    print(SenDat.__str__())
                    print('CurTemp - AvgValue =' + str(abs(self.curTemp - SenDat.getAvgValue())))
                    print('Threshold =' + str(self.alertDiff))
                    
                    if (abs(self.curTemp - SenDat.getAvgValue()) >= self.alertDiff):
                        print('The Current temperature exceeds average by >' + str(self.alertDiff) + 'TriggeringAlert...')
                        self.sensorData = SenDat.__str__()
                        SmtpClientConnector.publishMessage('Exceptional Sensor Data', self.sensorData) 
                    sleep(self.rateInSec)
                    
                
        
        