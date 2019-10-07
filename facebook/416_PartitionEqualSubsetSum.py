# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:26:39 2019

@author: huyn
"""

#416. Partition Equal Subset Sum
#Given a non-empty array containing only positive integers, find if the array can
# be partitioned into two subsets such that the sum of elements in both subsets is equal.
from typing import List
def canPartition(arr: List[int]) -> bool:
    s = sum(arr)
    if s%2:
        return False
    K = s//2
    row = len(arr)+1
    col = K+1
    dp =  [[False]*col for i in range(row)]
    for r in range(row):
        dp[r][0]=True
    for r in range(1,row):
        for c in range(1,col):
            dp[r][c] = dp[r-1][c] or dp[r-1][c-arr[r-1]]
    return dp[row-1][col-1]

arr=[1, 5, 11, 5]
print (canPartition(arr))
arr=[1, 2, 3, 5]
print (canPartition(arr))