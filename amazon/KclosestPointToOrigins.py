# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:54:16 2019

@author: huyn
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        myList = []
        for x,y in points:    
            distance = (x**2+y**2)
            heapq.heappush(myList,(distance,[x,y]))
        return [item[1] for item in heapq.nsmallest(K,myList)]