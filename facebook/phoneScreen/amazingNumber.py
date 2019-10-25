# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:13:47 2019

@author: huyn
"""
def maxOverlapping(intervals,start,stop):
    dictionary = {i:[0,0] for i in range(start,stop)}
    countOverlapping = 0
    res = None
    maxOverlap = 0
    
    for startIntewqrval,stopInterval in intervals:
        dictionary[startIntewqrval][0]+= 1
        dictionary[stopInterval][1]+= 1
            

    for i in range(start,stop):
        countOverlapping+= dictionary[i][0]
        if countOverlapping > maxOverlap:
            maxOverlap = countOverlapping
            res = i 
        countOverlapping-= dictionary[i][1]

    return res

def computeIntervals(array):
    size = len(array)
    intervals = []
    for index,num in enumerate(array):
        if num < size:
            if index >= num: # itself is a good one
                intervals.append([0,index-num])
                if index<size-1:
                    intervals.append([index+1,size-1])
            else: # if index < num, we have to shift 0 to left, which means our 0 have to be from the right
                # have to shift 0 to the left the amount of num-index, 
                start = index+1
                # we check how many to the right can we do it, basically
                stop = size - (num-index)
                intervals.append([start,stop])
                
        print (intervals)
    return intervals