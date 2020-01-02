# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:25:56 2020

@author: huyn
"""

#3Sum Closest
#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is 
#closest to target. 
#Return the sum of the three integers. You may assume that each input would have exactly one solution.
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        currentSum = float("inf")
        nums.sort()
        for index,num in enumerate(nums):
            i,j = index+1,len(nums)-1
            while i <j:
                first,last = nums[i],nums[j]
                s = num+first+last
                if abs(s-target)<abs(currentSum-target):
                    currentSum = s
                if s == target:
                    return target
                elif s<target:
                    i+=1
                else:
                    j-=1
        return currentSum