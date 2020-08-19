#! /usr/bin/env python     

import rospy
from std_msgs.msg import Int64




def publis():
    pub=rospy.Publisher('first_topic',Int64,queue_size=10)
    rospy.init_node('first',anonymous=True)
   
    
    
   
    pubint=int(raw_input())
    pub.publish(pubint)
   
   
    print "num is %s" %(pubint)
    
    
    
if __name__ =='__main__':
    try:
        publis()
    except rospy.ROSInterruptException:
        pass

