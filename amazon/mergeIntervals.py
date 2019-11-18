# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:28:56 2019

@author: huyn
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        currentInterval = intervals[0]
        output = []
        for interval in intervals[1:]:
            currentStart,currentStop = currentInterval
            start,stop = interval
            if currentStart<=stop:
                if currentStop<start: 
                    output.append(currentInterval)
                    currentInterval = interval
                else:
                    currentInterval = [min(start,currentStart),max(currentStop,stop)]
    #        print (currentInterval)
        output.append(currentInterval)
        return output        