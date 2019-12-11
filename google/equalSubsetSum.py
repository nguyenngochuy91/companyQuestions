# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:19:04 2019

@author: huyn
"""

#Equal Subset Sum Partition
def can_partition(num):
  # TODO: Write your code here
        
    s = sum(num)
    if s%2:
        return False
    def dfs(s,index):
        if index>=len(num):
            return False
        val = num[index]
        if val == s:
            return True
        elif val<s:
            check1 = dfs(s-val,index+1)
            check2 = dfs(s,index+1)
            return check1 or check2
        else:
            return dfs(s,index+1)
      
    return dfs(s//2,0)
      


def can_partition_topDown(nums):
    s = sum(nums)
    if s%2:
        return False
    dp = [[False for i in range(s//2+1)] for j in range(len(nums))] # set up as not visited
    def dfs(index,target):
        if index<len(nums):
            if dp[index][target]!= -1:
                return dp[index][target]
            else:
                val = nums[index]
                if val == target:
                    dp[index][target] = True
                elif val<target:
                    dp[index][target] = dfs(index+1,target-val) or dfs(index+1,target)
                else:
                    dp[index][target] = dfs(index+1,target-val)
        else:
            dp[index][target] = False
        return dp[index][target]
    dfs(0,s//2)
    return dp[0][s//2]
print (can_partition([1, 2, 3, 4]))
print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
print("Can partition: " + str(can_partition([2, 3, 4, 6])))