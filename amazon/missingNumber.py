# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:59:19 2020

@author: huyn
"""

#Missing Number
#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        return size*(size+1)//2-sum(nums)