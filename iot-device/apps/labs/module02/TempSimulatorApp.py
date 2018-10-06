'''
Created on Sep 15, 2018

@author: stannis
'''
from time import sleep
from labs.module02 import TempSensorEmulator

tempSensorEmulator = TempSensorEmulator.TempSensorEmulator()

tempSensorEmulator.daemon = True
print('-----------------')
print('Starting system performance and daemon thread')
tempSensorEmulator.enableEmulator = True

tempSensorEmulator.start()

while (True):
    sleep(10)
    pass