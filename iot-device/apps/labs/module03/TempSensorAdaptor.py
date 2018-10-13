'''
Created on Oct 08, 2018

@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/iot-device/apps')
from labs.common import SensorData
from labs.module02 import SmtpClientConnector
from cgitb import enable
from labs.module01.SystemPerformanceAdaptor import DEFAULT_RATE_IN_SEC
from random import random
from random import uniform
from builtins import str
from time import sleep
import threading

SenDat = SensorData.SensorData()
SmtpClientConnector = SmtpClientConnector.SmtpClientConnector()


class TempSensorAdaptor(threading.Thread):
    enableEmulator = False
    PrevTempSet = False
    rateInSec = 2
    
    SenDat.setName('Temperature')
    
    lowVal = 5
    highVal = 30
    alertDiff = 1
    curTemp = 0
    nomialTemp = 20
    
    
    def __init__(self, rateInSec):
        super(TempSensorAdaptor, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        
    def getCurrentValue(self):
        return self.curTemp


    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = uniform(float(self.lowVal), float(self.highVal))
                SenDat.addValue(self.curTemp)
                
                print('\n------------')
                #print('Sensor reading:')
                #print(' ' + str(self.curTemp))
                
                if self.PrevTempSet == False:
                    self.prevTempS = self.curTemp
                    self.PrevTempSet = True
                
                else: 
                    print(SenDat.__str__())
                    print('The Difference between CurTemp - NomialTemp:' + str(abs(self.curTemp - self.nomialTemp)))
                    print('The Threshold is:' + str(self.alertDiff))
                    print('\n')
                    #if (str(abs(self.curTemp - self.nomialTemp())) >= self.alertDiff):
                    if (abs(self.curTemp - self.nomialTemp) >= self.alertDiff):
                        print('The Current temperature exceeds the Nomial temperature by >' + str(self.alertDiff) + 'TriggeringAlert...')
                        self.sensorData = SenDat.__str__()
                        #SmtpClientConnector.publishMessage('Exceptional Sensor Data', self.sensorData) 
                    #sleep(self.rateInSec)
                    sleep(2)
            
            