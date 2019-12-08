# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:17:11 2019

@author: huyn
"""

#280. Wiggle Sort
#Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return