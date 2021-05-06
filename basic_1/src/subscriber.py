#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(msg):
    rospy.loginfo('{} x 3 = {}'.format(msg.data, 3.00 * msg.data))

def subscriber():
    # Initialize & Setup Node (NodeName)
    rospy.init_node("basic_1_sub")

    # Set listen topic (TopicName, MessageType)
    rospy.Subscriber("basic_1", Float32, callback)

    # start ROS node
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except Exception:
        print('Exception raised..')
