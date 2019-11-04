# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:44:43 2019

@author: huyn
"""
"""
1246. Palindrome Removal
Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] 
where i <= j, and remove that subarray from the given array. Note that after removing a subarray, 
the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array."""
from typing import List
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        size = len(arr)
        dp = [[float("inf")]*size for i in range(size)]
        for left in range(size-1,-1,-1):
            for right in range(left,size):
                if left == right:
                    dp[left][right] = 1
                else:
                    if arr[left] == arr[right]:
                        dp[left][right] = dp[left+1][right-1]
                    else:
                        dp[left][right] = min(dp[left+1][right]+1,dp[left][right-1]+1)
        return dp[0][size-1]