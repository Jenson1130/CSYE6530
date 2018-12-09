'''
Created on Oct 06, 2018

@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/zexin/iot-device/apps')
from time import sleep
from sense_hat import SenseHat
import threading
       
class SenseHatLedActivator(threading.Thread):
    enableLed  = False
    rateInSec  = 2
    rotateDeg  = 270
    sh = None 
    displayMsg = None
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
              
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
              
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
           
    def run(self):
        runnin = True
        print("6")
        while runnin:
            if self.enableLed:
                print("4")
                if self.displayMsg != None:
                    print("5")
                    self.sh.show_message(str(self.displayMsg))
                    runnin = False
                else:
                    self.sh.show_letter(str('R'))
                    runnin = False
                            
                    sleep(self.rateInSec)
                    self.sh.clear()
            sleep(self.rateInSec)
           
    def getRateInSeconds(self):
        return self.rateInSec
    
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
           
    def setDisplayMessage(self, msg):
        self.displayMsg = msg