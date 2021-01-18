import rospy
from task_2.msg import nameAndAge


def sendAgain():
    pass

def callback(msg):
    print(msg)
    print(f'Name : {msg.name} , Age : {msg.age}')


if __name__ == '__main__':

    rospy.init_node("Output",anonymous=True)
    rospy.Subscriber("three-tier", nameAndAge, callback)
    

    rospy.spin()