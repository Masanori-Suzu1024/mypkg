#!/usr/bin/env python3
import rospy 
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

if __name__== '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('twice', Int32, queue_size=10)
    rate = rospy.Rate(1)
    a = 0
    while not rospy.is_shutdown():
    
        a = a + n
        pub.publish(a)
        rate.sleep()
