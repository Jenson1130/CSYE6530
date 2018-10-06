'''
Created on Sep 15, 2018

@author: stannis
'''
import configparser
from builtins import str

config = configparser.ConfigParser()


class ConfigUtil():
    def __init__(self, fileAddr):
        self.fileAddr = fileAddr
        print('-----------Environment Setting------------')
        print('Already get the config' + str(self.fileAddr))
        
        
    def loadConfig(self):
        self.config = config.read(self.fileAddr)
        print('Already get the config' + str(self.config))
        
    def getProperty(self,section,key):
        self.key = key 
        
        return self.key
        
    


