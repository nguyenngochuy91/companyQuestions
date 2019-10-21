# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:55:40 2019

@author: huyn
"""

#Jump Game
#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.

from typing import List
def canJump(nums: List[int]) -> bool:
    # set up our min index to reach last as len(nums)-1
    minIndex = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        # get the step we can jump from here
        step = nums[i]
        # we update our closest index to jump to if we can reach the last using this index 
        if i+step>=minIndex:
            minIndex = i
    return minIndex ==0 

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]