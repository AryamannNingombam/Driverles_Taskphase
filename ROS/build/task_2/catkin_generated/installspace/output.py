#!/usr/bin/env python2

import rospy
from task_2.msg import nameAge,eligibility



def callback(msg):
 
    print(msg.data)
    print('Name ' + msg.data.person.name + ' | Age : ' + str(msg.data.person.age))
    print(msg.data.eligi)

if __name__ == '__main__':
    rospy.init_node("printNode",anonymous=True)
    rospy.Subscriber("sendEligibility",eligibility, callback)
    
    rospy.spin()
    
