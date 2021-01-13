#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32MultiArray



def callback(msg):
    firstNumber,secondNumber = msg.data
    print("First number : " + str(firstNumber) + " | Second number : " + str(secondNumber) + " | Sum : " + str(firstNumber+secondNumber))

def run():
    rospy.init_node("output",anonymous=True)
    rospy.Subscriber("getSum", Float32MultiArray, callback)
    rospy.spin()
   
    

if __name__ == '__main__':
    run()

    


