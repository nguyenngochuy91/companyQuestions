# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 00:08:36 2019

@author: huyn
"""

def subset_sum(nums,target):
    def dfs(index,currentTarget):
        if index>=len(nums):
            return False
        else:
            val = nums[index]
            if val== currentTarget:
                return True
            elif val<target:
                return dfs(index+1,currentTarget-val) or dfs(index+1,currentTarget)
            else:
                return dfs(index+1,currentTarget)
    return dfs(0,target)

def subset_sum_topDown(nums,target):
    dp = [[-1 for i in range(target+1)] for j in range(len(nums))]
    def dfs(index,currentTarget):
        if index<len(nums):
            if dp[index][currentTarget] == -1:
                val = nums[index]
                if val == currentTarget:
                    dp[index][currentTarget] = True
                elif val<currentTarget:
                    dp[index][currentTarget] = dfs(index+1,currentTarget-val) or dfs(index+1,currentTarget)
                else:
                    dp[index][currentTarget] = dfs(index+1,currentTarget)
            return dp[index][currentTarget]
        return False
    dfs(0,target)
#    print (dp)
    return dp[0][target]

print("Can partition: " + str(subset_sum_topDown([1, 2, 3, 7], 6)))
print("Can partition: " + str(subset_sum_topDown([1, 2, 7, 1, 5], 10)))
print("Can partition: " + str(subset_sum_topDown([1, 3, 4, 8], 6)))