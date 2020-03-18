# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:58:21 2020

@author: huyn
"""

#1060. Missing Element in Sorted Array
#Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.
from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        start, stop = 0 , len(nums)-1
        while start +1 <stop:
            mid = (start+stop)//2
            missing = findNumberMissing(nums,mid)
            if missing == k:
                return nums[start] + (k-findNumberMissing(nums,start))
            elif missing < k:
                start = mid
            else:
                stop = mid
        if k > findNumberMissing(nums,stop):
            return nums[stop]+ (k-findNumberMissing(nums,stop))
        return nums[start] + (k-findNumberMissing(nums,start))
def findNumberMissing(nums,currentIndex):
    return nums[currentIndex] - nums[0] -currentIndex