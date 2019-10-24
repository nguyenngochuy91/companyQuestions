# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 02:27:24 2019

@author: Huy Nguyen
"""

#Maximum Product Subarray
from typing import List
import random
def maxProduct(nums: List[int]) -> int:
    if len(nums) ==1:
        return nums[0]
    currentMax = - float("inf")
    countNeg  = 0
    accumulate, lastPart,lastIndex = 1,1,None
    for index,num in enumerate(nums):
        if num!=0:
            if num < 0 and countNeg == 0:
                lastPart = accumulate*num
                lastIndex = index
            if num < 0:
                countNeg+=1
            accumulate*= num
            print (16,index,num,accumulate,currentMax)
            currentMax = max(currentMax,accumulate)
        else:
            # we check if countNeg is divisible by 2
            if countNeg%2 and index-lastIndex>1:
                
                currentMax = max(currentMax,accumulate//lastPart)
            # reset the accumulate and lastPart
            countNeg = 0
            accumulate, lastPart = 1,1
    if countNeg%2 and index-lastIndex>=1:
        currentMax = max(currentMax,accumulate//lastPart)
    if currentMax<0 and 0 in nums:
        return 0
    return max(currentMax,accumulate//lastPart)
                
            
def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-3,3))
    return arr
for i in range(50):
    arr = generate(3)
    print (arr)