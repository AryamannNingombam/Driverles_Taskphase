#!usr/bin/env python


import rospy 


def pub():
    name = input("Enter the name of the person : ")
    age = int(input("Enter the age of the person : "))
    publishingObject = rospy.Publisher("three-tier", type, queue_size=10)
    rospy.init_node("Input",anonymous=True)
    publishingObject.publish()



if __name__ == '__main__':
    pub