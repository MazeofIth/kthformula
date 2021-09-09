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

## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic
#help from the youtube video

import rospy
from std_msgs.msg import Float32
import csv
import random

def callback(data):
    global x_value #global global global!!!
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    q = 0.15
    resultq = data.data/q
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    rate = rospy.Rate(20) # 20 messages per second
    pub.publish(resultq)
    csv_file = open('/home/elias/kthfsdv/data.csv', 'a')
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # should you use with open
    info = {
        "x_value": x_value,
        "resultq": resultq        }

    csv_writer.writerow(info)
    #print(x_value, total_1, total_2)

    x_value += 1
    #csv_file.flush()
    csv_file.close()

    rate.sleep()


fieldnames = ["x_value", "resultq"]

x_value = 0
print(x_value)
with open('/home/elias/kthfsdv/data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

def nodeB():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('nodeB', anonymous=True)

    rospy.Subscriber('edgren', Float32, callback) #!!! it's an int, not a String

    # spin() simply keeps python from exiting until this node is stopped
    #while not rospy.is_shutdown():
    rospy.spin()

if __name__ == '__main__':
    nodeB()
