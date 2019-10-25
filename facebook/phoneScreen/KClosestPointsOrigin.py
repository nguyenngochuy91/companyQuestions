# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:20:07 2019

@author: huyn
"""
from typing import List
#973. K Closest Points to Origin
import heapq
def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    myList = []
    for x,y in points:    
        distance = (x**2+y**2)
        heapq.heappush(myList,(distance,[x,y]))
    return [item[1] for item in heapq.nsmallest(K,myList)]
points = [[3,3],[5,-1],[-2,4]]
K= 2
print (kClosest(points,K))