# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:37:39 2019

@author: huyn
"""
"""
377. Combination Sum IV
Given an integer array with all positive numbers and no duplicates, find the number 
of possible combinations that add up to a positive integer target.
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        for val in range(1,target+1):

            for num in nums:
                if val<num:
                    break
                else:
          
                    dp[val] += dp[val-num]   

        return dp[target]