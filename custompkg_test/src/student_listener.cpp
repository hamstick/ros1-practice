#include <sstream>
#include <ros/ros.h>
#include <custom_msgs/Student.h>

void chatter_callback(const custom_msgs::Student& msg)
{
  ROS_INFO("---- STUDENT INFO ----");
  ROS_INFO("%s (%s)", msg.name.c_str(), msg.id.c_str());
  ROS_INFO("%d Credits (GPA: %.2f)", msg.credits, msg.gpa);

  return;
}

int main(int argc, char *argv[])
{
  ros::init(argc, argv, "cmsg_listener");
  ros::NodeHandle handle;

  ros::Subscriber sub = handle.subscribe("chatter", 1000, chatter_callback);
  ros::spin();

  return 0;
}
