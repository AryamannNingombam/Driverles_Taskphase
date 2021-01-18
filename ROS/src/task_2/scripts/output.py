#!/usr/bin/env python

import rospy
from task_2.msg import nameAge,eligibility
from std_msgs.msg import Bool


def callback(msg):
    print(msg)
    print(msg.data)


if __name__ == '__main__':
    rospy.init_node("printNode",anonymous=True)
    rospy.Subscriber("sendEligibility", Bool, callback)
    
    rospy.spin()
    
