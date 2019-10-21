# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:21:11 2019

@author: huyn
"""

#Missing Ranges
#Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
from typing import List
def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    res = []
    for num in nums:
        # check if num>lower, means we miss some number from lower to num-1
        if lower<num:
            if num-1 == lower:
                res.append(str(lower))
            else:
                res.append("{}->{}".format(lower,num-1))
        lower = num + 1
    # once we hit the last num, we check wether our lower is still less than upper
    if lower <= upper:
        if upper == lower:
            res.append(str(lower))
        else:
            res.append("{}->{}".format(lower,upper))
    return res
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99