#!/usr/bin/env python2
import rospy 
from task_2.msg import nameAge



def pub():
    publishingObject = rospy.Publisher("sendNameAge", nameAge, queue_size=10)
    rospy.init_node("Input",anonymous=True)

    #name = input("Enter the name of the person : ")
    age = int(input("Enter the age of the person : "))
   
    temp = nameAge("Aryamann",age)



    publishingObject.publish(temp)



if __name__ == '__main__':
    pub()
