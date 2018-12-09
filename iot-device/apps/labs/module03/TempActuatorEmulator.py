'''
Created on Oct 08, 2018

@author: stannis
'''
# from labs.common.SensorData import SensorData
# import sense_hat
# from labs.common import ConfigUtil
# from labs.module03 import SmtpClientConnector
# from random import uniform
# from time import sleep
# from threading import Thread
# from labs.module01.SystemPerformanceAdaptor import DEFAULT_RATE_IN_SEC
# from importlib.resources import path
import os,sys
sys.path.append('/home/pi/Desktop/zexin/iot-device/apps')
from labs.module03 import SimpleLedActivator
from labs.module03 import SenseHatLedActivator
from labs.common import ActuatorData

class TempActuatorEmulator:
    tempActuatorData = None
    simledActivator = None
    senledActivator = None
    
    def __init__(self):
        self.tempActuatorData = ActuatorData.ActuatorData()
        
        self.simledActivator = SimpleLedActivator.SimpleLedActivator()
        self.simledActivator.daemon = True
        self.simledActivator.start()
        
        self.senledActivator = SenseHatLedActivator.SenseHatLedActivator()
        self.senledActivator.daemon = True
        self.senledActivator.start()
        
    def process_message(self, ActuatorData):
        self.tempActuatorData.updateData(ActuatorData)
        self.simledActivator.setEnableLedFlag(True)
        self.SenAction(ActuatorData)
        
    def SenAction(self, msg):
        if self.tempActuatorData.getCommand() == 0:
            message = "The Temperature is Lower than The Nomial Temperature by:" + str(self.tempActuatorData.getValue())
            print(message)
            self.senledActivator.setEnableLedFlag(True)
            self.senledActivator.setDisplayMessage(msg)
            self.senledActivator.run()
        if self.tempActuatorData.getCommand() == 1:
            self.senledActivator.setEnableLedFlag(False)
            message = "The Temperature is Higher The Nomial Temperature by:" + str(self.tempActuatorData.getValue())
            print(message)
            self.senledActivator.setDisplayMessage(msg)
    
    
    
