# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:57:25 2019

@author: huyn
"""
import random
#253. Meeting Rooms II
#Given an array of meeting time intervals consisting of start and end times 
#[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
def minMeetingRooms(intervals):
    if len(intervals)<=1:
        return len(intervals)
    intervals.sort()
    count =0 
    d = {0: [intervals[0]]}
    for start,stop in intervals[1:]:
        # we check to see if we can add to the last of the list of a current room number
        currentMin = float("inf")
        roomNum    = None
        found      = False
        for num in range(count+1):
            lastStart,lastStop = d[num][-1]
            if start<lastStop:
                continue
            elif start == lastStop:
                d[num].append([start,stop])
                found = True 
                roomNum = None
                break
            else:
                val = start-lastStop
                if val<currentMin:
                    currentMin= val
                    roomNum   = num
                found = True
        # if roomNum == None means that dont find any room can store the start stop, initiate new
        if not found:
            count+=1
            d[count]= [[start,stop]]
        else:
            if roomNum!=None:
                d[roomNum].append([start,stop])
    return count+1
def generateTest(n):
    arr = []
    for i in range(n):
        start = random.randint(0,30)
        stop  = random.randint(start+1,start+30)
        arr.append([start,stop])
    return arr
#intervals = [[0, 30],[5, 10],[15, 20]]
#print (minMeetingRooms(intervals))
#intervals = [[7,10],[2,4]]
#print (minMeetingRooms(intervals))
intervals = generateTest(10000)
print (intervals)
#intervals = [[1, 28], [1, 29], [13, 28], [16, 29], [23, 31], [25, 45], [26, 48], [29, 44], [29, 54], [30, 34]]
print (minMeetingRooms(intervals))