#!/usr/bin/env python
import rospy
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

rospy.init_node('aiml_tty')
soundhandle = SoundClient()
rospy.sleep(1)
soundhandle.stopAll()
print('Starting TTS')

def pronounce(data):
    print(data)
    print(data.data)
    response = data.data
    rospy.loginfo('Response:: %s' % response)
    soundhandle.say(response)

def listener():
    rospy.loginfo('Starting listening to response')
    rospy.Subscriber('/response', String, pronounce, queue_size = 10)
    rospy.spin()

if __name__ == '__main__':
    listener()