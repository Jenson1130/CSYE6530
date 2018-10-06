'''
Created on Sep 15, 2018

@author: stannis
'''
from labs.common import ConfigUtil
from email.mime.multipart import MIMEMultipart
#from labs.module02.TempSensorEmulator import Sens
from test.test_enum import threading
from labs.common import ConfigConst
from email.mime.text import MIMEText
from builtins import str
import smtplib
#from nntplib import port
from labs.common import SensorData
#from smtplib import server, fromaddr


SenDat = SensorData.SensorData()


class SmtpClientConnector(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        
        
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
        """
        
        smtpServer = smtplib.SMTP_SSL(host, port) 
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken) 
        smtpServer.sendmail(fromAddr, toAddr, msgText) 
        smtpServer.close()
        """
        
        def mail():
            ret = True
            try:
                print('')
                print('The content of msgText:')
                print('-----------------------')
                print(str(msgText))
                print('-----------------------')
                server = smtplib.SMTP_SSL(host,port)
                #print(1)
                server.ehlo()
                #print(2)
                #server.starttls()
                server.login(fromAddr, authToken)
                #print(3)
                server.sendmail(fromAddr, toAddr, msgText)
                
                server.quit()
                server.close()
                
            except Exception:
                ret = False
            return ret
        
        
        ret = mail()
        if ret:
            print('-----------------------')
            print("The Alert-Email has been sent")
            print('-----------------------')
        else:
            print('-----------------------')
            print("Failed to send the Alert-Email!")
            print('-----------------------')
                
#server = smtplib.SMTP_SSL("smtp.mail.yahoo.com",465)
#print(1)
#server.ehlo()
#print(2)
#server.starttls()
#server.login("li.zexin@yahoo.com", "condevice")
#print(3)
#server.sendmail("li.zexin@yahoo.com", "jensonli1130@gmail.com", "msgText")
            
                
    
        