# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:10:36 2019

@author: huyn
"""

#Count of Subset Sum
def count_subsets(nums, s):
    count = 0
    def dfs(index,currentS):
        nonlocal count
        if index<len(nums):
            val = nums[index]
            if val+currentS == s:
                count +=1
            elif val+currentS<s:
                dfs(index+1,currentS+val)
                dfs(index+1,currentS)
            else:
                dfs(index+1,currentS)
    dfs(0,0)
    if s == 0:
        count +=1
    return count
    
#print("Total number of subsets " + str(count_subsets([-1, 1, 0, 2], 0)))
#print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
def count_subsets_topDown(nums, s):
    dp = [[-1 for i in range(s+1)] for j in range(len(nums))]
    def dfs(index,currentS):
        if index<len(nums):
            val = nums[index]
            if dp[index][currentS] == -1:
                if val+currentS == s:
                    dp[index][currentS] = 1+ dfs(index+1,currentS+val)
                elif val+currentS<s:
                    dp[index][currentS] = dfs(index+1,currentS+val) +dfs(index+1,currentS)
                else:
                    dp[index][currentS] = dfs(index+1,currentS)
            return dp[index][currentS]
        elif index == len(nums):
            return 0
    dfs(0,0)
#    print (dp)
    return dp[0][0]
    
print("Total number of subsets " + str(count_subsets_topDown([-1, 1, 0, 2], 0)))
#print("Total number of subsets: " + str(count_subsets_topDown([1, 2, 7, 1, 5], 9)))