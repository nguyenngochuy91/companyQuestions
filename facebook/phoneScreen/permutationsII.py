# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 01:22:55 2019

@author: huyn
"""

#Permutations II
def permuteUnique(nums):
    res = set()
    def dfs(index):
        if index == len(nums):
            res.add(tuple(nums[:]))
        else:
            for i in range(index,len(nums)):
                # we swap the index, we start at i == index so we keep the very first initial, no swapping
                # only swap if 2 number are different:
                if nums[i]!=nums[index] or i==index:
                    nums[index],nums[i] = nums[i],nums[index]
                    dfs(index+1)
                    nums[i],nums[index] = nums[index],nums[i]

    dfs(0)
    return [list(item) for item in res]
print (permuteUnique([1,1,2]))