'''
Created on Oct 08, 2018

@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/zexin/iot-device/apps')
from labs.module03 import TempSensorAdaptor
from labs.module03 import TempActuatorEmulator
from labs.module03 import MQTTClient
from labs.common import ActuatorData
from time import sleep
from builtins import int
from sense_hat import SenseHat


path = "/Users/stannis/eclipse-workspace2/iot-device/data/ConnectedDeviceConfig.props"

tempSensor = TempSensorAdaptor.TempSensorAdaptor(3)
tempSensor.enableEmulator = True
tempActuatorData = ActuatorData.ActuatorData()
tempActuatorEmulator = TempActuatorEmulator.TempActuatorEmulator();
tempSensor.start()
val = 0
senseHat = SenseHat()
client = MQTTClient.MQTTClient()
client.go()

