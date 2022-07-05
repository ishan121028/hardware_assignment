#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy

#---------------------------------------------------- 

class Drive:
    def __init__(self,driver1,driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2
         

    def drive_callback(self,inp):
        # A bit of help! These are arrays of data
        axes = inp.axes
        buttons = inp.buttons

        if buttons[0]:
            print("BACKWARD")
            self.rightClaw.BackwardM1(127)
            self.leftClaw.BackwardM1(127)
        if buttons[1]:
            print("RIGHT")
            self.rightClaw.ForwardM1(127)
            self.leftClaw.BackwardM1(127)
            
        if buttons[2]:
            print("LEFT")
            self.rightClaw.BackwardM1(127)
            self.leftClaw.ForwardM1(127)

        if buttons[3]:
            print("FORWARD")
            self.rightClaw.ForwardM1(127)
            self.leftClaw.ForwardM1(127)

    def current_limiter(self):
        """BONUS: 

        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        return False
                

#---------------------------------------------------                



