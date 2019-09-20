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
    def __init__(self,matrix,current,index=3):# facing up as initial
        self.matrix = matrix
        self.current = current
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)] # + means we turning right
        self.index      = index
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        addX,addY = self.directions[self.index]
        x,y       = self.current
        X,Y       = x+addX,y+addY
        if X>=0 and Y>=0 and X<len(self.matrix) and Y<len(self.matrix[0]):
            if self.matrix[X][Y]!=0:
                self.current = X,Y
                return True
        return False
    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        if self.index==0:
            self.index= 3
        else:
            self.index-=1
    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        if self.index==3:
            self.index= 0
        else:
            self.index+=1 

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        x,y = self.current
        self.matrix[x][y]="X" # the clean wont know this
#room = [
#  [1,1,1,1,1,0,1,1],
#  [1,1,1,1,1,0,1,1],
#  [1,0,1,1,1,1,1,1],
#  [0,0,0,1,0,0,0,0],
#  [1,1,1,1,1,1,1,1]
#]
#robot =Robot(room,[1,3])
#print (robot.current)
#print (robot.move())
#print (robot.current)
#robot.turnLeft()
#print (robot.move())
#print (robot.current)
#robot.turnRight()
#print (robot.move())
#print (robot.current)
#robot.turnLeft()
#print (robot.move())
#print (robot.current)
#robot.turnLeft()
#print (robot.move())
#print (robot.current)

def cleanRoom(robot:Robot):
    """
    :type robot: Robot
    :rtype: None
    """
    visited= ()
    visited.add((0,0))
    notPossible = set()
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    currentIndex = 3
    # this is dfs, basically where we will traverse, keep track,clean the room
    def dfs(currentCell,path,direction):
        # we check all 4 cell around currentCell
        return
    return
