# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 04:19:16 2019

@author: huyn
"""
#3Sum
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res =set()
    check = set()
    for index,num in enumerate(nums):
        if num not in check:
            check.add(num)
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