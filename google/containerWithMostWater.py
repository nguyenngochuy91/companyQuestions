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
    # the idea is to find 2 point that has maximum width (x2-x1)*min(y1,y2)
    # basically, our problem can be solve using f(0,n) = max(f(0,n-1),min(y_n-1,y_n),xn*min*(y_0,y_n))
    currentMin = min(height[:2])
    for i in range(2,len(height)):
        currentMin = max(currentMin,min(height[i],height[i-1]),min(height[i],height[0])*i)
    return currentMin

height = [1,8,6,2,5,4,8,3,7]
print (maxArea(height))