# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 01:04:13 2019

@author: huyn
"""

#Permutations
def permute(nums):
    res = []
    def dfs(path):
        if len(nums)==0:
            res.append(path[:]) # deep copu
        else:

            for i in range(len(nums)):
                number = nums.pop(i)
                path.append(number)
                dfs(path)
                path.pop()
                nums.insert(i,number)
    dfs([])
    return res
def permuteSwap(nums):
    res = []
    def dfs(index):
        if index == len(nums):
            res.append(nums[:])
        else:
            for i in range(index,len(nums)):
                # we swap the index, we start at i == index so we keep the very first initial, no swapping
                nums[index],nums[i] = nums[i],nums[index]
                dfs(index+1)
                nums[i],nums[index] = nums[index],nums[i]
    dfs(0)
    return res
print (permuteSwap([1,2,3]))