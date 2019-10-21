# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:21:37 2019

@author: huyn
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:47:21 2019

@author: huyn
"""
#42. Trapping Rain Water
#Given n non-negative integers representing an elevation map where the width of 
#each bar is 1, compute how much water it is able to trap after raining.
# naive way, for each coloum, we count how much that column can store water by looking for max left 
# and max right
def trapNaive(height) -> int:
    rain = 0
    for index,water in enumerate(height):
        maxL = max(height[:index+1])
        maxR = max(height[index:])
        rain+= min(maxL,maxR)-water
    return rain

# using same idea, but store the maxL,maxR at each index
def trapDynamic(height):
    left = []
    for index,water in enumerate(height):
        if not left:
            left.append(water)
        else:
            left.append(max(left[-1],water))
    right = []
    for index in range(len(height)-1,-1,-1):
        water = height[index]
        if not right:
            right.append(water)
        else:
            right.append(max(right[-1],water))
    size = len(height)
    water= 0
    for i in range(size):
        water+=min(left[i],right[size-1-i])-height[i]
    return water
    
# using same idea, but with pointers
def trapPointers(height):
    water= 0
    return water
height=[0,1,0,2,1,0,1,3,2,1,2,1]
#print (trapNaive(height))
#print (trapDynamic(height))