#!/usr/bin/env python3

# BSD 3-Clause "New" or "Revised" License 
# Copyright (c) 2021, Masanori-Suzu1024 RyuichiUeda
# All rights reserved.
# Genshin is a copyrighted work of miHoYo co., Ltd

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=10)
rate = rospy.Rate(1)
n = 0
val = input('Enter character`s strength: ')
c_strength = int(val)
print(val)
val = input('Enter arms strength: ')
a_strength = int(val)
print(val)
val = input('Enter Tenp magnification(%):')
tenp = float(val)
print(val)
val = input('Enter damage buf(%):')
damage_buf = float(val)
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
damage = base_damage * critical_correct * (damage_buf / 100)
print('base_damage:')
print(base_damage)
print('critical correction value(ideal value):')
print(critical_correct)
print('total_damage:')
print(damage)
n = int(damage)

while not rospy.is_shutdown():

    pub.publish(n)
    rate.sleep()
