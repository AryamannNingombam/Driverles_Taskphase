#!/usr/bin/env python

import rospy
from task_2.msg import nameAge,eligibility



def callback(msg):
 
 
    print('Name ' + msg.person.name + ' | Age : ' + str(msg.person.age))
    print(msg.eligi)
if __name__ == '__main__':
    rospy.init_node("printNode",anonymous=True)
    rospy.Subscriber("sendEligibility",eligibility, callback)
    
    rospy.spin()
    
