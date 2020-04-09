#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('lcdscreen', String, queue_size=10)
    rospy.init_node('sample_publisher', anonymous=True)

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():

        test = "hi Dylan :)"
        rospy.loginfo(test)
        pub.publish(test)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#for more on python publishers, wiki.ros.org
