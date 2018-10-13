'''
Created on Sep 15, 2018

@author: stannis
'''
import configparser
import os

Default_CONFIG_FILE = '/home/pi/Desktop/iot-device/data/ConnectedDeviceConfig.props'

class ConfigUtil():
    configfile = Default_CONFIG_FILE
    configdata = configparser.ConfigParser()
    isLoaded   = False
    
    def __init__(self,configFile):
        print(configFile)
        if(configFile != ''):
            print('hello')
            self.configfile = configFile
    
    def loadConfig(self):
        print(Default_CONFIG_FILE)
        if(os.path.exists(self.configfile)):
            self.configdata.read(self.configfile)
            self.isLoaded = True
    
    def getConfig(self, forceReload = False):
        if(self.isLoaded == False or forceReload):
            self.loadConfig()
        return self.configdata
    
    def getConfigFile(self):
        return self.configfile

    def getProperty(self,section, key, forceReload = False):
        return self.getConfig(forceReload).get(section, key)
    
    def isConfigDataLoaded(self):
        return self.isLoaded
    


