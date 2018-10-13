'''
Created on Sep 15, 2018

@author: stannis
'''
import os
from datetime import datetime
from builtins import str

class SensorData():
    '''
    classdocs
    '''
    timeStamp = None
    name = 'Not Set'
    curValue = 0
    avgValue = 0
    minValue = 0
    maxValue = 0
    totValue = 0
    sampleValue = 0
    sampleCount = 0

    def __init__(self):
        self.timeStamp = str(datetime.now())
        
        '''
        Constructor
        '''
    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        
        self.totValue = self.totValue +newVal
        self.curValue = newVal
        
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
        if (self.totValue != 0 and self.sampleValue > 0):
            self.avgValue = self.totValue / self.sampleValue
    
    def getAvgValue(self):
        return self.avgValue
    
    def getMaxValue(self):
        return self.maxValue
    
    def getMinValue(self):
        return self.minValue
    
    def getValue(self):
        return self.curValue
    
    def gettotValue(self):
        return self.totValue
    
    def setName(self, name):
        self.name = name
        
    def __str__(self):
        customStr = \
            str(self.name + ':'  + \
            os.linesep + '\tTime:'   + self.timeStamp + \
            os.linesep + '\tCurrent:' + str(self.curValue) + \
            #os.linesep + '\tAverage:' + str(self.avgValue) + \
            #os.linesep + '\tSamples:' + str(self.sampleValue) + \
            os.linesep + '\tMinimum:' + str(self.minValue) + \
            os.linesep + '\tMaximum:' + str(self.maxValue))
        return customStr                              
    
    
            
    
        