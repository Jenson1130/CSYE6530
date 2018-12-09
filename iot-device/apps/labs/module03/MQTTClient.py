'''
Created on Dec 7, 2018
 
@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/zexin/iot-device/apps')
import paho.mqtt.client as mqttClient
from labs.module03 import SenseHatLedActivator
class MQTTClient():   
    def on_connect(self, clientConn, data, flags, resultCode):
        print("Client connected to server. Result: " + str(resultCode))
        clientConn.subscribe("myActuatorData")
        
    def on_message(self,clientConn, data, msg):
        print("Received PUBLISH on topic {0}. Payload: {1}".format(str(msg.topic), str(msg.payload)))
        senledActivator = SenseHatLedActivator.SenseHatLedActivator()
        print(msg.payload)
        senledActivator.setDisplayMessage(msg.payload)
        senledActivator.setEnableLedFlag(True)
        senledActivator.run()
        
    def go(self):
        self.mc = mqttClient.Client()
        self.mc.on_connect = self.on_connect
        self.mc.on_message = self.on_message
         
        self.mc.connect("test.mosquitto.org", 1883, 60)
        self.mc.loop_forever()
 
