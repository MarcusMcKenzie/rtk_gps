#!/usr/bin/env python
import sys
import serial, string, math, time, struct 
import socket #
import time
import rospy #
import utm  
from sensor_msgs.msg import NavSatFix

class SerialReader(object): 
    
    def __init__(self,port_name,BaudRate): 

        self.port = serial.Serial(port_name, baudRate, timeout=1)  

        self.gpsPub = rospy.Publisher('rtk_fix', NavSatFix, queue_size=1)
        
        self.gpsData = NavSatFix()
                
               
 
    def readloop(self):
  
        while True:      
         rate = rospy.Rate(10)
                 
                    
         line = self.port.readline()
     
         if line.startswith('$GPGGA'):

                 gpsvals = line.strip().split(',')
                            

                 lat = (float(gpsvals[2])%100)/60 + float(gpsvals[2])//100
                 if gpsvals[3] == 'S': 
                    lat*=-1

                 lon  = (float(gpsvals[4])%100)/60 + float(gpsvals[4])//100
                 if gpsvals[5] == 'W':
                    lon*=-1
            
                
                 self.gpsData.latitude = float(lat)
                
                 self.gpsData.longitude = float(lon)
                
                 self.gpsData.altitude = float(gpsvals[9])
                 
                                   
                
                 self.gpsPub.publish(self.gpsData)
                 
                 rospy.loginfo("GPS Data %s", self.gpsData)

                 rate.sleep()
                

if __name__ == "__main__":
 
    try:    

        portName = rospy.get_param('port_name', '/dev/ttyACM0') 

        baudRate = rospy.get_param('baud_rate', 115200)
 
        mySr = SerialReader(portName, baudRate)

        rospy.init_node('gpsdata', anonymous=True)     

        mySr.readloop()


    except rospy.ROSInterruptException:
    
        pass
