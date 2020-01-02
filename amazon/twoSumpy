# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:29:42 2020

@author: huyn
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,num in enumerate(nums):
            if target - num in d:
                return [d[target-num][0],index]
            if num not in d:
                d[num] = []
            d[num].append(index)
