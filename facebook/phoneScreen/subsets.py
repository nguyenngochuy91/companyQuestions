# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 01:38:35 2019

@author: huyn
"""

#Subsets
def subsets(nums):
    if not nums:
        return []
    res = [[]]
    for num in nums:
        temp = []
        for item in res:
            temp.append(item[:])
            item.append(num)
            temp.append(item[:])
        res = temp
    return res
print (subsets([1,2,3]))