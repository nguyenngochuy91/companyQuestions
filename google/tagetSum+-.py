# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:30:54 2019

@author: huyn
"""

#Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign.
# We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.
def targetSum(nums,S):
    count = 0
    def dfs(currentIndex,accumulate):
        nonlocal count
        if currentIndex == len(nums):
            if accumulate == S:
                count += 1
        else:
            val = nums[currentIndex]
            dfs(currentIndex+1,accumulate+val)
            dfs(currentIndex+1,accumulate-val)
    dfs(0,0)
    return count
    
print("Total ways: " + str(targetSum([1, 1, 2, 3], 1)))
print("Total ways: " + str(targetSum([1, 2, 7, 1], 9)))
