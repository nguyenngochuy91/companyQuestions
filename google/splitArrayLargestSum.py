# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 03:17:42 2019

@author: Huy Nguyen
"""

#Split Array Largest Sum
#Given an array which consists of non-negative integers and an integer m, you can
# split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
#
#Note:
#If n is the length of array, assume the following constraints are satisfied:
#
#1 ≤ n ≤ 1000
#1 ≤ m ≤ min(50, n)
from typing import List
def splitArray(nums: List[int], m: int) -> int:
    return