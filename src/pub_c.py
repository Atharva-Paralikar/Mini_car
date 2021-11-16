#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def talker():
    
    rospy.init_node('turtlebot_teleop')

    pub_move = rospy.Publisher('/proj1/f_controller/command', Float64, queue_size=10)
    pub_move1 = rospy.Publisher('/proj1/r_controller/command', Float64, queue_size=10)
    pub_move2 = rospy.Publisher('/proj1/l_controller/command', Float64, queue_size=10) 
    
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        hello_str = "Moving Forward %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        
        pub_move1.publish(20) 
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
