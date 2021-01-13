#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray


def runInput():
    pub = rospy.Publisher("getSum",Float64MultiArray,queue_size=10)
    rospy.init_node("Input",anonymous=True)
    while not rospy.is_shutdown():
        firstNumber = int(input("Enter the first number : "))
        secondNumber = int(input("Enter the second number : "))
        pub.publish([firstNumber,secondNumber])



if __name__ == '__main__':
    try:
        runInput()
    except rospy.ROSInterruptException:
        print("Error!")