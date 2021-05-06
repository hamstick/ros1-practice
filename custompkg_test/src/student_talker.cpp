#include <sstream>
#include <ros/ros.h>
#include <custom_msgs/Student.h>

int main(int argc, char *argv[])
{
  int i = 0;
  ros::init(argc, argv, "cmsg_talker");
  ros::NodeHandle handler;
  ros::Publisher pub = handler.advertise<custom_msgs::Student>("chatter", 10); // Publisher

  ros::Rate loop_rate(1); // how many times in 1sec. [Hz]
  while(ros::ok()){
    custom_msgs::Student msg;
    msg.id = "AL17083";
    msg.name = "Koki Nagahama";
    msg.credits = 130;
    msg.gpa = 3.20;

    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}

