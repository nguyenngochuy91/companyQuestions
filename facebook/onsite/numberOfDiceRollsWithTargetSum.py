# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:12:59 2019

@author: huyn
"""
"""
1155. Number of Dice Rolls With Target Sum
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll 
the dice so the sum of the face up numbers equals target.
"""
class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if target<d:
            return 0
        elif target == d:
            return 1
        dp = {}
        def dfs(acc,index,target,d,f):
            if index == d:
                if acc == target:
                    return 1
                else:
                    return 0
            else:
                if index in dp:
                    if acc in dp[index]:
                        return dp[index][acc]
                count = 0
                for num in range(1,f+1):
                    count += dfs(acc+num,index+1,target,d,f)
                if index not in dp:
                    dp[index] = {}
                if acc not in dp[index]:
                    dp[index][acc] = count
                return count % (10**9+7)
        res =  dfs(0,0,target,d,f)
        return res