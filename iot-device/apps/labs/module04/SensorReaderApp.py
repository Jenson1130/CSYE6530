'''
Created on Oct 12, 2018

@author: stannis
'''
from time import sleep
import os,sys
sys.path.append('/home/pi/Desktop/iot-device/apps')
from labs.module04 import I2CSenseHatAdaptor

TempAd = I2CSenseHatAdaptor.I2CSenseHatAdaptor()


print("Starting...")

TempAd.enableEmulator = True
TempAd.daemon = True
TempAd.start()

while (True):
    sleep(5)
    pass
