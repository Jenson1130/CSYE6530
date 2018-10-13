'''
Created on Oct 08, 2018

@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/iot-device/apps')
from labs.module03 import TempSensorAdaptor
from labs.module03 import TempActuatorEmulator
from labs.common import ActuatorData
from time import sleep
from builtins import int



path = "/Users/stannis/eclipse-workspace2/iot-device/data/ConnectedDeviceConfig.props"

tempSensor = TempSensorAdaptor.TempSensorAdaptor(2)
tempSensor.enableEmulator = True

tempActuatorData = ActuatorData.ActuatorData()

tempActuatorEmulator = TempActuatorEmulator.TempActuatorEmulator();

tempSensor.start()
val = 0
while True:
    val =  str(tempSensor.nomialTemp - tempSensor.curTemp)
    tempActuatorData.setValue(val)
    if tempSensor.curTemp > int(tempSensor.nomialTemp):
        tempActuatorData.setCommand(1)
    if tempSensor.curTemp < int(tempSensor.nomialTemp):
        tempActuatorData.setCommand(0)
        
    tempActuatorEmulator.process_message(tempActuatorData)
    sleep(5)
    