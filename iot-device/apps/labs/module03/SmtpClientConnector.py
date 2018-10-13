'''
Created on Oct 08, 2018

@author: stannis
'''
import os,sys
sys.path.append('/home/pi/Desktop/iot-device/apps')
from labs.common import ConfigUtil
from labs.common import ConfigConst
import smtplib
from email.mime.text import MIMEText
from labs.common import SensorData
from email.mime.multipart import MIMEMultipart

SData = SensorData.SensorData()
 
class SmtpClientConnector:
    smtpConfigReader = None
    
    
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('')
        self.config.loadConfig()
        print('Configuration data is...\n' + str(self.config))
        
        
    def publishMessage(self, topic, data):
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)

        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic 
        msgBody = str(data)
        print('****************')
        print(msg['From'])
        print(msg['To'])
        msg.attach(MIMEText(msgBody)) 
        msgText = msg.as_string()
        
        # send e-mail notification
        
        
        server = smtplib.SMTP_SSL(host, port) 
        server.ehlo()
        server.login(fromAddr, authToken) 
        server.sendmail(fromAddr, toAddr, msgText) 
        server.close()
        print('---------------------------')
        print('The content of msgText:')
        print(str(msgText))
        print('Successful! The E-mail has been sent!')
        print('---------------------------')