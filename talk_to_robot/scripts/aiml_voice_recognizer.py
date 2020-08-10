#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('aiml_voice_recognizer.py')
pub = rospy.Publisher('voiceWord', String, queue_size = 10)
r = rospy.Rate(1)

def transferCallback(data):
    print(data)
    text = data.data
    rospy.loginfo("I received data : %s" % text)
    pub.publish(text)

def transferTopic():
    rospy.loginfo('Starting topic transfer node!')
    rospy.Subscriber('/recognizer/output', String, transferCallback, queue_size = 10)
    rospy.spin()

transferTopic()