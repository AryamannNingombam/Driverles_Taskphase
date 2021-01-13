#!/usr/bin/env python


import rospy
from std_msgs.msg import Float64MultiArray

def callback(msg):
    
    rospy.loginfo(f'The message is {str(msg)}')


def runOutput():
    rospy.init_node("Output",anonymous=True)
    rospy.Subscriber("getSum", Float64MultiArray, callback)
    
    
    
    rospy.spin()

if __name__ == '__main__':
    runOutput()