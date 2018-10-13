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
sys.path.append('/home/pi/Desktop/iot-device/apps')
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
        self.SenAction()
        
    def SenAction(self):
        if self.tempActuatorData.getCommand() == 0:
            message = "The Temperature is Lower than The Nomial Temperature by:" + str(self.tempActuatorData.getValue())
            print(message)
            self.senledActivator.setEnableLedFlag(True)
            print("1")
            self.senledActivator.setDisplayMessage(message)
            print("2")
            self.senledActivator.run()
            print("3")
        if self.tempActuatorData.getCommand() == 1:
            self.senledActivator.setEnableLedFlag(False)
            message = "The Temperature is Higher The Nomial Temperature by:" + str(self.tempActuatorData.getValue())
            print(message)
            self.senledActivator.setDisplayMessage(message)
    
    
    
#     enableTempEmulator = False
#     tempSenData = SensorData()
#     rateInSec = DEFAULT_RATE_IN_SEC
#     PrevTempS = False
#     
#     lowVal = 5
#     highVal = 30
#     alertDiff = 5
#     
#     curTemp = 0
#     minValue = 0
#     maxValue = 0
#     nomialTemp = 10
#     #minUpdateTime = 0
#     #maxUpdateTime = 0
#     emailSender = None
#     SenHat = None
#     devConfigRead = None
#     
#     
#     
#     
#     
#     def __init__(self, maxTemp, minTemp):
#         Thread.__init__(self)
#         
#         self.minValue = minTemp
#         self.maxValue = maxTemp
#         
#         self.devConfigRead = ConfigUtil.ConfigUtil('')
#         self.enableTempEmulator = self.devConfigRead.getProperty('device', "enableEmulator")
#         self.nomialTemp = self.devConfigRead.getProperty('device', "nomialTemp")
#         print(self.nomialTemp)
#         self.SenHat = sense_hat.SenseHat()
#         
#     def getCurValue(self):
#         return self.curTemp
#     
#     def run(self):
#         while True:
#             if self.enableEmulator == "True":
#                 self.curTemp = uniform(float(self.minValue), float(self.maxValue))
#                 self.tempSenData.addValue(self.curTemp)
#                 
#                 if self.PrevTempSet == False:
#                     self.prevTempS = self.curTemp
#                     self.PrevTempS = True
#             else:
#                 print("Sense_Hat")
#                 self.curTemp = self.SenHat.get_temperature()
#                 self.tempSenData.addValue(self.curTemp)
#             
#             print('\n------------')
#             print('Sensor reading:')
#             print(' ' + str(self.curTemp))
#             
#             print(SensorData.__str__())
#             print('CurTemp - AvgValue =' + str(abs(self.curTemp - SensorData.getAvgValue())))
#             print('Threshold =' + str(self.alertDiff))
#                     
#             if (abs(self.curTemp - SensorData.getAvgValue()) >= self.alertDiff):
#                 print('The Current temperature exceeds average by >' + str(self.tempSenData.avgValue - self.curTemp) + 'TriggeringAlert...')
#                 self.sensorData = SensorData.__str__()
#                 #SmtpClientConnector.publishMessage('Exceptional Sensor Data', self.sensorData) 
#                 path = "/Users/stannis/eclipse-workspace2/iot-device/data/ConnectedDeviceConfig.props"
#                 emailSender = SmtpClientConnector.SmtpClientConnector(path)
#                 emailSender.sendEmailMessage("Exceptional Sensor Data", self.tempSenData)
#                 
#             
#             sleep(self.rateInSec)
    
# devConfigRead = ConfigUtil.ConfigUtil("/Users/stannis/eclipse-workspace2/iot-device/data/ConnectedDeviceConfig.props")
# enableTempEmulator = devConfigRead.getProperty("device","key","forceReload")
# nomialTemp = devConfigRead.getProperty("nomialTemp")
# print(nomialTemp)