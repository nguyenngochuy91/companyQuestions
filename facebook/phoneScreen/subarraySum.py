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
    # solve by checking accumulate
    # initialize of dictionary that store how many time before a certain continous array from 0 to i,j,k,... sums up to value x
    dictionary = {}
    # store 0 as 1, for case like k= 1 , nums[0] = 1
    dictionary[0]=1
    currentSum = 0
    count = 0
    for num in nums:
        currentSum +=num
        val = currentSum -k
        if val in dictionary:
            count+=dictionary[val] # we add to the count how may time it can form a continous subs array
        if currentSum not in dictionary:
            dictionary[currentSum]= 0
        dictionary[currentSum]+=1 # we increase number of contnous array have same sum
   
        return count

def generateTest(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-10,10))
    return arr

arr,k = generateTest(100),random.randint(1,100)
print (arr,k)
