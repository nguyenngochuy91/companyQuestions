# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:46:45 2019

@author: huyn
"""

#Point in max overlapping intervals
#Given number M and N intervals in the form [a, b] (inclusive) where for every
# interval -M <= a <= b <= M, create a program that returns a point where the maximum number of intervals overlap.
input =[[0,2],[0,2],[2,4],[3,8],[5,10]]
def find(M,intervals):
    d = {}
    for i in range(-M,M+1):
        d[i]=0
    for start,stop in intervals:
        d[start]+=1
        d[stop]-=1
    currentOverlap, currentMax = 0,0
    for key in range(-M,M+1):
        currentOverlap+=d[key]
        if currentOverlap>currentMax:
            output = key
            currentMax = currentOverlap
    return output

print (find(10,input))
# if one end at time t1, and another start at time t1, the end at t1 does not account overlap
def findAllNotCountingTouch(M,intervals):
    d = {}
    for i in range(-M,M+1):
        d[i]=0
    for start,stop in intervals:
        d[start]+=1
        d[stop]-=1
    currentOverlap, currentMax = 0,0
    arr = []
    for key in range(-M,M+1):
        # when hitting a key that has more stop than end, and our currentOverlap was equal to currentMax
        # this indicate our max interval coming to an end
        if d[key]<0 and currentOverlap==currentMax:
            arr.append([start,key])
            # reset start
            start = None
        # if our currentOverlap == currentMax -1 
        currentOverlap+=d[key]
        if currentOverlap>currentMax:
            # reset our array
            arr =[]
            start = key
            currentMax = currentOverlap
        # if we start hitting our max again
        elif currentOverlap==currentMax and start == None:
            start = key
            stop  = key
                
    return arr
#print (findAllNotCountingTouch(10,input))

# if one end at time t1, and another start at time t1, the end at t1 does account for overlap
def findAllCountingTouch(M,intervals):
    d = {}
    for i in range(-M,M+1):
        d[i]=[]
    for start,stop in intervals:
        d[start].append(1)
        d[stop].append(-1)
    currentOverlap, currentMax = 0,0
    arr = []
    for key in range(-M,M+1):
        # check len of our d[key]
        if len(d[key])>currentMax:
            # if it combines of stop and start, then it is just a small t1,t1 
            currentMax = len(d[key])
            if -1 in d[key]:
                arr= [[key,key]]
            else:
                start = key
        val = sum(d[key])
        # when hitting a key that has more stop than end, and our currentOverlap was equal to currentMax
        # this indicate our max interval coming to an end
        if val<0 and currentOverlap==currentMax:
            arr.append([start,key])
            # reset start
            start = None
        # if our currentOverlap == currentMax -1 
        currentOverlap+=val
        if currentOverlap>currentMax:
            # reset our array
            arr =[]
            start = key
            currentMax = currentOverlap
        # if we start hitting our max again
        elif currentOverlap==currentMax and start == None:
            start = key
            stop  = key
                
    return arr
#print (findAllCountingTouch(10,input))