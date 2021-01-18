#!/usr/bin/env python

import rospy
from task_2.msg import nameAge,eligibility
from std_msgs.msg import Bool


def publish(name,age):

    message_pub = rospy.Publisher("sendEligibility", Bool, queue_size=10)
    print("PUBLISHING!")

    if age< 18:
        message_pub.publish(Bool(data=False))
    else:
        message_pub.publish(Bool(data=True))



def callback(msg):
   
    print('Name'+ ': '+msg.name+' , Age : ' + str(msg.age))
    publish(msg.name,msg.age)
 

if __name__ == '__main__':

    rospy.init_node("Output",anonymous=True)
    rospy.Subscriber("sendNameAge", nameAge, callback)
    

    rospy.spin()
