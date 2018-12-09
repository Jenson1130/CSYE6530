'''
Created on Oct 12, 2018

@author: stannis
'''
from time import sleep

from labs.module04 import I2CSenseHatAdaptor

TempAd = I2CSenseHatAdaptor.I2CSenseHatAdaptor()


print("Starting...")

TempAd.enableEmulator = True
TempAd.daemon = True
TempAd.start()

while (True):
    sleep(5)
    pass
