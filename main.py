#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from gpiozero import Motor
import pygame

motor00 = Motor(5, 6) #front left wheel
motor01 = Motor(16, 12) #front right wheel
motor10 = Motor(20,21) #back left wheel
motor11 = Motor(19,26) #back right wheel


#node
'''
def mPublisher(Motor active):
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    mForward()
    mPublisher.setup(flListener,GPIO.out)
    mPublisher.setup(frListener,GPIO.out)
    mPublisher.setup(blListener,GPIO.out)    
    mPublisher.setup(brListener,GPIO.out)

def flListener(): 
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('flchatter', String, callback)

def frListener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('frchatter', String, callback)


def blListener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('blchatter', String, callback)

def brListener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('brchatter', String, callback)

    '''
#node that enables and disables the motors :D
def mForward(Motor active):
    active.forward()

def mBackward(Motor active):
    active.backward()



def basicForward():
    mForward(motor00)
    mForward(motor01)
    mForward(motor10)
    mForward(motor11)
    

def turnLeft():
    #

def turnRight():
    #

def basicBackward():
    

if __name__ == '__main__':

    