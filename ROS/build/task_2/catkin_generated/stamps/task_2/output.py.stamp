#!/usr/bin/env python

import rospy
from task_2.msg import nameAge
from std_msgs import Bool


def callback(msg):
    print(msg)
    print(msg.data)


if __name__ == '__main__':
    rospy.Subscriber("sendEligibility", Bool, callback)
    