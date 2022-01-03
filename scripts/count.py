#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    val = input(' Enter character`s strength: ')
    c_strength = int(val)
    print(val)
    val = input(' Enter arms strength: ')
    a_strength = int(val)
    print(val)
    val = input(' Enter Tenp magnification(%):')
    tenp = float(val)
    print(val)
    base_damage = (c_strength + a_strength) * tenp / 100
    print(base_damage)

    val = input('Enter Critical rate(%):')
    critical_rate = float(val)
    print(val)
    val = input('Enter Critical damage magnification(%):')
    critical_damage = float(val)
    print(val)
    critical_correct = 1 + ((critical_rate / 100) * (critical_damage / 100))
    print(critical_correct)




    pub.publish(n)
    rate.sleep()
