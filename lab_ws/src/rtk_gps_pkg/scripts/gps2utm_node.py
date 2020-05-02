#!/usr/bin/env python
import sys
import serial
import time
import rospy
import utm
import std_msgs.msg
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Point


class UTM():
    
    
          
    def __init__(self):              
                             

                self.utmPub = rospy.Publisher('utm_fix', Odometry, queue_size=1)

                self.utmData = Odometry()

                rospy.init_node('gps', anonymous=True)

                rospy.Subscriber("rtk_fix", NavSatFix, self.callback)
    
                rospy.spin()               

                       

    def callback(self,data): 
         
       
                rate = rospy.Rate(10)
                
                lat = float(data.latitude) 
               
                lon = float(data.longitude)

                alt = float(data.altitude)

                               
                easting, northing, zonenum, zonelet = utm.from_latlon(lat,lon)

                x = float(easting)

                y = float(northing)

                z = float(alt) 


   
                self.utmData.pose.pose.position = Point(x,y,z) 

                self.utmPub.publish(self.utmData)

                rospy.loginfo("UTM Data %s", self.utmData)

                rate.sleep()


if __name__ == '__main__':
    
    try:                              
               nUTM = UTM()
       
               rospy.spin()           
                  
    except rospy.ROSInterruptException:

              pass
