#!/usr/bin/env python

import rospy
import cv2 as cv
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


def callback(msg):
    bridge = CvBridge()
 
    frame = bridge.imgmsg_to_cv2(msg)
    name = "Subscribed Image"
    cv.namedWindow(name)
    cv.imshow(name,frame)
    cv.waitKey(3)




def run():
    rospy.init_node("image_sub",anonymous=True)
    rospy.Subscriber("/camera/color/image_raw",Image,callback)
    rospy.spin()


if __name__ == '__main__':
    run()