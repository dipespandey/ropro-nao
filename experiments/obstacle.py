# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:44:10 2019
@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:08:52 2019
@author: Lenovo
"""
#openpyxl for raeding excel files

import argparse
import time
from naoqi import ALProxy
import sys
import math
import csv

thres = 0.3
def main(robot_IP, robot_PORT=9559):
    tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
    motion = ALProxy("ALMotion", robot_IP, robot_PORT)
    memory = ALProxy("ALMemory", robot_IP, robot_PORT)
    sonar = ALProxy("ALSonar", robot_IP, robot_PORT)
    postureProxy=ALProxy("ALRobotPosture", robot_IP, robot_PORT)
   # tts.say("Nice to meet you, where you been? I could show you incredible things Magic, madness, heaven, sin Saw you there and I thought Oh my God, look at that face You look like my next mistake Love's a game, wanna play? New money, suit and tie I can read you like a magazine Ain't it funny, rumors fly And I know you heard about me So hey, let's be friends I'm dying to see how this one ends Grab your passport and my hand I can make the bad guys good for a weekend ")
    # Wake up robot
    tts.say("Hi! I'm Nao. How are all of you today? LET'S WALK")
    motion.wakeUp()
    # Send robot to Pose Init
    #postureProxy.goToPosture("StandInit", 0.5)

	#except Exception, e:
	#	print "Could not create proxy by ALProxy"
	#	print "Error was: ", e
	# ----------> <----------

	# Subscribe to sonars, this will launch sonars (at hardware level)
	# and start data acquisition.
    #sonar.subscribe("myApplication")
    cnt=0

    while(True):
        sonar.subscribe("myApplication")

        LeftSonar=memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
        RightSonar=memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")

        if(LeftSonar==5.0 or RightSonar==5.0):
            continue
        
        if(LeftSonar<thres or RightSonar<thres):
            x=0.0
            y=0.0
            theta  = -(math.pi/2)
        
            tts.say('Oops! I detected something in front of me.')
            motion.moveTo(x, y, theta)
            
            LeftSonar=memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
            RightSonar=memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
            if(LeftSonar<thres and RightSonar<thres):
                x=0.0
                y=0.0
                theta=math.pi
                motion.moveTo(x, y, theta)
                LeftSonar=memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
                RightSonar=memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
                if(LeftSonar<thres and RightSonar<thres):
                     x=0.0
                     y=0.0
                     theta  = (math.pi/2)
                     print('Turn Left')
                     tts.say('Oops! I detected something in front of me.')
                     print(LeftSonar)
                     print(RightSonar)
                     motion.moveTo(x, y, theta)
                else:
                     x=0.1
                     y=0.0
                     theta=0
                     motion.moveTo(x, y, theta)
                     print('Move Straight3')
                     
                     continue
            else:
                 x=0.1
                 y=0.0
                 theta=0
                 motion.moveTo(x, y, theta)
                 print('Move Straight2')
                 print(LeftSonar)
                 print(RightSonar)
                 continue
        else:
           x=0.05
           y=0.0
           theta=0
           motion.moveTo(x, y, theta)
           print('Move Straight1')
           print(LeftSonar)
           print(RightSonar)
           continue
           
        cnt+=1
        sonar.unsubscribe("myApplication")
            
        
		#time.sleep(0.5)

	# Unsubscribe from sonars, this will stop sonars (at hardware level)
	#sonar.unsubscribe("myApplication")

	# Please read Sonar ALMemory keys section
	# if you want to know the other values you can get.

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="192.168.137.202", help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	main(args.ip, args.port)