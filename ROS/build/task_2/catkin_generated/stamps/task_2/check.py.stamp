#!/usr/bin/env python
from ROS.src.task_2.scripts.input import pub
import rospy
from task_2.msg import nameAge
from std_msgs import Bool


def publish(name,age):

    message_pub = rospy.Publisher("sendEligibility", Bool, queue_size=10)
    rospy.init_node("eligibilityPublisher",anonymous=True)

    if age< 18:
        message_pub.publish(Bool(data=False))
    else:
        message_pub.publish(Bool(data=True))



def callback(msg):
    print(msg)
    print('Name'+ ': '+msg.name+' , Age : ' + str(msg.age))
    publish(msg.name,msg.age)

if __name__ == '__main__':

    rospy.init_node("Output",anonymous=True)
    rospy.Subscriber("sendNameAge", nameAge, callback)
    

    rospy.spin()
