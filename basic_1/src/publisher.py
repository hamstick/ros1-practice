#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import Float32

def publisher():
    # Initialize node (NodeName, anonymous)
    rospy.init_node("basic_1_pub")

    # Initialize topic (TopicName, MessageType)
    pub = rospy.Publisher("basic_1", Float32, queue_size = 10)

    # Set publish cycle
    rate = rospy.Rate(1)
    
    count = 0
    while not rospy.is_shutdown():
        # create publish message
        msg = Float32()
        msg.data = random.uniform(-100.00, 100.00)

        # send message
        pub.publish(msg)

        count += 1
        rospy.loginfo("count: {} -> message_value: {}".format(count, msg.data))
        rate.sleep()

if __name__ == '__main__':
    random.seed(None)
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

