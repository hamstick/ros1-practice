#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher():
    # Initialize node (NodeName, anonymous)
    rospy.init_node("helloworld_pub")

    # Initialize topic (TopicName, MessageType)
    pub = rospy.Publisher("hw_topic", String, queue_size = 10)

    # Set publish cycle
    rate = rospy.Rate(1)
    
    count = 0
    while not rospy.is_shutdown():
        msg_text = "hello world"
        
        # create publish message
        msg = String()
        msg.data = rospy.get_param('~message')

        # send message
        pub.publish(msg)

        count += 1
        rospy.loginfo("count: {} -> message: {}".format(count, msg_text))
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

