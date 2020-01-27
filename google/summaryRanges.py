#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 00:29:21 2020

@author: huynguyen
"""


# 228. Summary Ranges
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        string = str(nums[0])
        currentNum = nums[0]
        length = 1
        for num in nums[1:]:
            if currentNum+1 == num:
                currentNum = num
                length +=1
            else:
                if length >1:
                    string += "->"+ str(currentNum)
                res.append(string)
                currentNum = num
                string = str(currentNum)
                length = 1
        if length >1:
            string += "->"+ str(currentNum)
        res.append(string)
        return res