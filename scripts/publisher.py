#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('lcdscreen1', String, queue_size=10)
    rospy.init_node('sample_publisher1', anonymous=True)

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():

        test = "test1"
        rospy.loginfo(test)
        pub.publish(test)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#for more on python publishers, wiki.ros.org
