# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:21:50 2019

@author: huyn
"""

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    dictionary = {}
    for start,stop in intervals:
        if start not in dictionary:
            dictionary[start]= 0
        dictionary[start]+=1
        if stop not in dictionary:
            dictionary[stop]= 0
        dictionary[stop]-=1
    myList = sorted(dictionary)
    currentRoom, minRoom = 0,0
    for time in myList:
        currentRoom+=dictionary[time]
        minRoom= max(minRoom,currentRoom)
    return minRoom