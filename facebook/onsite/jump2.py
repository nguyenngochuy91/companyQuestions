# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:18:20 2019

@author: huyn
"""
"""
45. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

"""

nums = [2,3,1,1,4]
class Solution(object):
    def jump(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln <= 1:
            return 0
        
        cnt = till = 0
        maxIdx = 0 
        for i in range(ln):
            maxIdx = max(maxIdx, i + nums[i])
            if i == till:
                cnt += 1
                till = maxIdx 
            
            if till >= ln-1:
                return cnt