#! /usr/bin/env python  

import rospy
from std_msgs.msg import Int64

def callback(data):
    rospy.loginfo("the num is squaring %s" %(data))
    
    passint=data.data*data.data
    pubs=rospy.Publisher('second_topic',Int64,queue_size=10)
    pubs.publish(passint)
    print "publishing"
   
    
def square():
    rospy.init_node('second',anonymous=True)
    rospy.Subscriber('first_topic',Int64,callback)
    
    rospy.spin()
if __name__=='__main__':
    square()


