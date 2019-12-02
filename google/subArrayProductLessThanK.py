# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:41:07 2019

@author: huyn
"""

#713. Subarray Product Less Than K
#
#
#Your are given an array of positive integers nums.
#
#Count and print the number of (contiguous) subarrays where the product of all 
#the elements in the subarray is less than k.
from typing import List
class Solution:
    def numSubarrayProductLessThanKLog(self, nums: List[int], k: int) -> int:
        return