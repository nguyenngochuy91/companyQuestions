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
    visited= set()
    visited.add((0,0))
    # we clean the current cell
    robot.clean()
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    currentIndex = 3
    def proceed(currentCell,currentIndex):
        x,y = currentCell
        if robot.move():
            # compute the cell cordinate
            addX,addY = directions[currentIndex]
            # check if this cell already fully visited
            X,Y = x+addX,y+addY
            newCell = (X,Y)
#                print ("newCell",newCell)
            if (X,Y) not in visited:
                # we clean this tile
                robot.clean()
                dfs(newCell,currentIndex)
                # after dfs, we have to go back ward for the robot
                # we turn left twice and move
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
                    # now we are back to our currentCell for our robot and with the same direction
#        print (127,currentCell)
    # this is dfs, basically where we will traverse, keep track,clean the room
    def dfs(currentCell,currentIndex):
        # we check all 4 cell around currentCell
        # we will try to move away from our position 3 times
        # move forward
        visited.add(currentCell)
        x,y = currentCell
#        print (133,currentCell,robot.current)
        for i in range(4):
            proceed(currentCell,currentIndex)
            currentIndex= (currentIndex+1)%4
#            print (137,currentCell,robot.current)
            robot.turnRight()
#            if i==1:
#                break

        
    dfs((0,0),currentIndex)
    print (robot.matrix)
#room =[[1,1,1],[1,1,1],[1,1,1]]
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
]
robot =Robot(room,[2,2])
cleanRoom(robot)
