'''
Created on Oct 08, 2018

@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/zexin/iot-device/apps')
from labs.common import SensorData
#from labs.module02 import SmtpClientConnector
from cgitb import enable
from random import random
from random import uniform
from builtins import str
from time import sleep
import threading
from sense_hat import SenseHat
from labs.module03 import CoapClientConnector

##from labs.module04 import I2CSenseHatAdaptor

SenDat = SensorData.SensorData()


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
    
    coapclient = CoapClientConnector.CoapClientConnector()
    
    
    def __init__(self, rateInSec):
        super(TempSensorAdaptor, self).__init__()
        self.coapClientConnector = CoapClientConnector.CoapClientConnector()
        self.sh = SenseHat()
        
##        self.i2CSenseHatAdapter = I2CSenseHatAdaptor()
##        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        
    def getCurrentValue(self):
        return self.curTemp


    def run(self):
        while True:
            
##                self.curTemp = self.sh.get_temperature()
            self.curTemp = 233
            SenDat.addValue(self.curTemp)
            #self.coapclient.handlePostTest("temp", self.curTemp)
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
                self.val =  self.sh.get_temperature()
                self.coapClientConnector.handlePostTest("zexinTemp", str(self.val))
        sleep(1)
            
            