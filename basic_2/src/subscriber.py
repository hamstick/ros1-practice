#!/usr/bin/env python3

import datetime as dt
import rospy
from std_msgs.msg import String

def callback(msg):
  dt_now = dt.datetime.now()
  if msg.data == "date":
    rospy.loginfo("I heard msg: {} --> {}".format(msg.data, dt_now.strftime("%Y/%m/%d")))
  elif msg.data == "time":
    rospy.loginfo("I heard msg: {} --> {}".format(msg.data, dt_now.strftime("%H:%M:%S")))
  else:
    rospy.loginfo("I heard msg: {} --> No message is returnable".format(msg.data))

def subscriber():
  rospy.init_node("basic_2_sub")
  rospy.Subscriber("basic_2", String, callback)
  rospy.spin()

if __name__ == '__main__':
  try:
    subscriber()
  except Exception:
    print('Exception raised..')

