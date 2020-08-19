#! /usr/bin/env python  

import rospy
from std_msgs.msg import Int64

def callback(data):
    rospy.loginfo("the Squared num is %s" %(data.data))

def printing():
    rospy.init_node('third',anonymous=True)
    rospy.Subscriber('second_topic',Int64,callback)

    rospy.spin()
if __name__=='__main__':
    printing()

