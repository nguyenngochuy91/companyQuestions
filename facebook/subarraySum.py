# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:05:34 2019

@author: huyn
"""
import random
#560. Subarray Sum Equals K
#Given an array of integers and an integer k, you need to find the total number
# of continuous subarrays whose sum equals to k.
def subarraySum( nums, k) -> int:
    d= {0:1}
    count = 0
    current =0
    for num in nums:
        current+=num
        val = current-k
        if val in d:
            count+=d[val]
        if current not in d:
            d[current]=0
        d[current]+=1
        
    return count

def generateTest(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-10,10))
    return arr

arr,k = generateTest(100),random.randint(1,100)
print (arr,k)
