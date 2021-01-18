#!usr/bin/env python


import rospy 
from task_2.msg import nameAndAge

def pub():
    name = input("Enter the name of the person : ")
    age = int(input("Enter the age of the person : "))
    publishingObject = rospy.Publisher("three-tier", nameAndAge, queue_size=10)
    rospy.init_node("Input",anonymous=True)
    temp = nameAndAge()
    temp.name = name
    temp.age = age
    publishingObject.publish(temp)



if __name__ == '__main__':
    pub