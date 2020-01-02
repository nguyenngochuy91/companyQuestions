# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:07:24 2020

@author: huyn
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =set()
        for index,num in enumerate(nums):
            start,stop = index+1,len(nums)-1
            s = -num
            while start<stop:
                val = nums[start]+nums[stop]
                if val==s:
                    res.add((num,nums[start],nums[stop]))
                    start+=1
                    stop-=1
                elif val<s:
                    start+=1
                else:
                    stop-=1
            
        return [list(item) for item in res]