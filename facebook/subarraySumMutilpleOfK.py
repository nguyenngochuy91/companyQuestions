# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:38:09 2019

@author: Huy Nguyen
"""
import random
#523. Continuous Subarray Sum
#Given a list of non-negative numbers and a target integer k, write a function to 
#check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.
def checkSubarraySum(nums,k):
    d = {}
    s = 0
    for i in range(len(nums)):
        if i==0:
            try:
                s=nums[i]%k
                
            except:
                s= nums[i]
            d[s]=[0]
        else:
            try:
                s= (s+nums[i])%k
            except:
                s+=nums[i]
            if s==0:
                return True
            if s not in d:
                d[s]=[]

            # check if index at least 2
            for index in d[s]:
                if abs(index-i)>=2:
                    return True
            d[s].append(i)
    return False

def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-10,30))
    return arr
nums,k = generate(100),100000
print (nums)
print (k)

