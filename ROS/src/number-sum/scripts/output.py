#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32MultiArray



def callback(msg):
    rospy.loginfo(f"The message recieved is {msg}")
    
    

if __name__ == '__main__':


    rospy.init_node("output",anonymous=True)
    rospy.Subscriber("getSum", Float32MultiArray, callback)
    rospy.spin()


