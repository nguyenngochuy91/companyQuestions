# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:19:13 2019

@author: huyn
"""

#56. Merge Intervals
#Given a collection of intervals, merge all overlapping intervals.
def merge(intervals):
    if len(intervals)<=1:
        return intervals
    # sort the interval
    intervals.sort()
    currentInterval = intervals[0]
    output = []
    for interval in intervals[1:]:
        currentStart,currentStop = currentInterval
        start,stop = interval
        # if current interval start less or equal to stop
        if currentStart<=stop:
            # for case where they dont overlap [1,3], [5,6]
           # we can also can check max(start,currentstart)>min(stop,currentStop) for overlap
            if currentStop<start: 
                output.append(currentInterval)
                currentInterval = interval # update our currentInterval
            else:
                # our new interval get to merge
                currentInterval = [min(start,currentStart),max(currentStop,stop)]
#        print (currentInterval)
    output.append(currentInterval) # append the current one
    return output
intervals = [[1,3],[2,6],[8,10],[15,18]]
print ("output:",merge(intervals))
intervals = [[1,4],[4,5]]
print (merge(intervals))