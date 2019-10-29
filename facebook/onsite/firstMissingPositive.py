# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:57:29 2019

@author: huyn
"""
"""
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer."""
import random
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mySet = set()
        for num in nums:
            if num>0:
                mySet.add(num)
        res = 1
        while True:
            if res not in mySet:
                return res
            res+=1
        return res
    def faster(self,nums):
        return
        
def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-20,20))
    return arr
for i in range(10):
    print (generate(10))