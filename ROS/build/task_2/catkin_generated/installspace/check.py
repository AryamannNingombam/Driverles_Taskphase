#!/usr/bin/env python2

import rospy
from task_2.msg import nameAge,eligibility



def publish(msg):

    message_pub = rospy.Publisher("sendEligibility", eligibility, queue_size=10)
    print("PUBLISHING!")

    if age< 18:
        message_pub.publish(eligibilty(msg,'Not eligible'))
    else:
        message_pub.publish(eligibility(msg,'eligible'))



 

if __name__ == '__main__':

    rospy.init_node("Output",anonymous=True)
    rospy.Subscriber("sendNameAge", nameAge, publish)
    

    rospy.spin()
