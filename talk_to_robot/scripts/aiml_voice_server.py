#!/usr/bin/env python
import rospy
import os
import sys
import aiml
from std_msgs.msg import String

rospy.init_node('aiml_voice_server')
mybot = aiml.Kernel()
pub = rospy.Publisher('response', String, queue_size = 10)

def load_aiml(aiml_file):
    aiml_path = rospy.get_param('aiml_path')
    print(aiml_path)
    print(aiml_file)
    os.chdir(aiml_path)
    if os.path.isfile('standard.brn'):
        mybot.bootstrap(brainFile = 'standard.brn')
    else:
        mybot.bootstrap(learnFiles = aiml_file)
        mybot.saveBrain('standard.brn')

def callback(data):
    input = data.data
    response = mybot.respond(input)

    rospy.loginfo('I received %s' % input)
    rospy.loginfo('I said %s' % response)
    pub.publish(response)

def listener():
    rospy.loginfo('Starting aiml server node!')
    rospy.Subscriber('voiceWord', String, callback)
    rospy.spin()

if __name__ == '__main__':
    load_aiml(rospy.get_param('aiml_file'))
    listener()