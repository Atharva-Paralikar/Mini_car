#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/proj1/r_controller/command", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
