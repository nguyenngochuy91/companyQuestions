# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:58:58 2019

@author: huyn
"""

#Maximize Distance to Closest Person
#In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
#
#There is at least one empty seat, and at least one person sitting.
#
#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#
#Return that maximum distance to closest person.
def maxDistToClosest(seats):
    dp = [[float("inf"),float("inf")] for i in range(len(seats))]
    left = None
    for i in range(len(seats)):
        if seats[i] == 1:
            left = i
        else:
            if left == None and i!= 0:
                dp[i][0] = i
            elif left!= None:
                dp[i][0] = i - left
    right = None
    for i in range(len(seats)-1,-1,-1):
        if seats[i] == 1:
            right = i
        else:
            if right == None and i!= len(seats)-1:
                dp[i][1] = len(seats)-1-i
            elif right!= None:
                dp[i][1] = right - i  
    currentBest = -float("inf")
#    print (dp)
    for i in range(len(dp)):
        left,right = dp[i]
        best = min(left,right)
        if best!= float("inf") and best>currentBest:
            currentBest = best
    return currentBest
print (maxDistToClosest([1,0,0,0,1,0,1]))
print (maxDistToClosest([0,1]))
