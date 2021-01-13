#!/usr/bin/env python


import rospy as ros
from std_msgs.msg import Float32MultiArray



def main():
    pub = ros.Publisher("getSum", Float32MultiArray, queue_size=10)
    
    ros.init_node("input",anonymous=True)
    firstNumber = int(input("Enter the first number : "))
    secondNumber = int(input("Enter the second number : "))
    timer = ros.Rate(10)
    while not ros.is_shutdown():
        pub.publish(Float32MultiArray(data=[firstNumber,secondNumber]))
        timer.sleep()

if __name__ == '__main__':
    try:
        main()
    except ros.ROSInterruptException:
        print("ERROR!")
