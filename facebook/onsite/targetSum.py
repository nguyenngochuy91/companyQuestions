# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:11:48 2019

@author: huyn
"""
"""
494. Target Sum
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
"""
class Solution(object):
    def findTargetSumWaysBackTrack(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        def dfs(index,acc,S):
            if index == len(nums):
                if acc == S:
                    self.count += 1
            else:
                num = nums[index]
                dfs(index+1, acc+num,S)
                dfs(index+1, acc-num,S)
        dfs(0,0,S)
        return self.count
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        def dfs(index,acc,S):
            if index == len(nums):
                if acc == S:
                    self.count += 1
            else:
                num = nums[index]
                dfs(index+1, acc+num,S)
                dfs(index+1, acc-num,S)
        dfs(0,0,S)
        return self.count