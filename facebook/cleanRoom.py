# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:48:03 2019

@author: huyn
"""

#489. Robot Room Cleaner
#Given a robot cleaner in a room modeled as a grid.
#
#Each cell in the grid can be empty or blocked.
#
#The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
#
#When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
#
#Design an algorithm to clean the entire room using only the 4 given APIs shown below.
 """
 This is the robot's control interface.
 You should not implement it, or speculate about its implementation
 """
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """

def cleanRoom(self, robot):
    """
    :type robot: Robot
    :rtype: None
    """