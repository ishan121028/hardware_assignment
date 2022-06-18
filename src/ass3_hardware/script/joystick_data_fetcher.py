#!/usr/bin/python
import pygame
import time
from std_msgs import String

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
axes = joystick.get_numbuttons()

while True:
    time.sleep(1)
    for i in range(axes):
            button = joystick.get_button(i)
            if(i==3 and button == 1): print("FORWARD")
            if(i==2 and button == 1): print("LEFT")
            if(i==0 and button == 1): print("DOWN")
            if(i==1 and button == 1): print("RIGHT")

def talker():
    pub = rospy.Publisher('/joy', String, queue_size=10)
    rospy.init_node('key_mapping', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        for i in range(axes):
            button = joystick.get_button(i)
            if(i==3 and button == 1): 
                temp = "FORWARD"
                rospy.loginfo(temp)
                pub.publish(temp)
            if(i==2 and button == 1):
                temp = "LEFT"
                rospy.loginfo(temp)
                pub.publish(temp)
            if(i==0 and button == 1):
                temp = "DOWN"
                rospy.loginifo(temp)
                pub.publish
            if(i==1 and button == 1):
                temp = "RIGHT"
                rospy.loginfo(temp)
                pub.publish(temp)
    rate.sleep()

if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
          pass




    

