# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 03:13:31 2019

@author: huyn
"""

#Container With Most Water
#Given n non-negative integers a1, a2, ..., an , where each represents a point 
#at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i 
#is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, 
#such that the container contains the most water.
#
#Note: You may not slant the container and n is at least 2.\
from typing import List
def maxArea(height: List[int]) -> int:
    i,j = 0 ,len(height)-1
    maxA = 0
    while i <j:
        maxA = max(maxA,(j-i)*min(height[i],height[j]))
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return maxA

height = [1,8,6,2,5,4,8,3,7]
print (maxArea(height))