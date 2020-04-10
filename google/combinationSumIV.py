#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:58:42 2020

@author: huynguyen
"""


# 377. Combination Sum IV
# Given an integer array with all positive numbers and no duplicates, find the 
# number of possible combinations that add up to a positive integer target.
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d ={0:1}
        def dfs(targetSum):
            if targetSum in d:
                return d[targetSum]
            else:
                val = 0
                for num in nums:
                    if targetSum - num>=0:
                        val +=dfs(targetSum-num)
                d[targetSum] = val
                return val
        return dfs(target)
        