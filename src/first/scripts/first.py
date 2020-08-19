#! /usr/bin/env python     

import rospy




def publis():
    pub=rospy.Publisher('first_topic',int)
    rospy.init_node('first',anonymous=True)
    
    
   
    pubint=raw_input()
    
   
    print ("num is"+pubint)
    pub.publish(pubint)
    
    
if __name__ =='__main__':
    try:
        publis()
    except rospy.ROSInterruptException:
        pass

