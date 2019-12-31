# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 00:35:44 2019

@author: huyn
"""

#Minimum Subset Sum Difference
def minSumDifference(nums):
    s = sum(nums)
    currentMin = float("inf")
    path = None
    def dfs(currentPath,currentSum,s,index):
        nonlocal currentMin
        nonlocal path
        if index<len(nums):
            left = s - currentSum- nums[index]
            dif = abs(left- currentSum- nums[index])
            if dif<currentMin:
                path = currentPath[:]
            currentMin = min(dif,currentMin)
            currentPath.append(nums[index])
            dfs(currentPath,currentSum+nums[index],s,index+1)
            currentPath.pop()
            dfs(currentPath,currentSum,s,index+1)
    dfs([],0,s,0)
    return currentMin,path

#print("Can partition: " + str(minSumDifference([1, 2, 3, 9])))
#print("Can partition: " + str(minSumDifference([1, 2, 7, 1, 5])))
#print("Can partition: " + str(minSumDifference([1, 3, 100, 4])))

def minSumDifference_topDown(nums):
    s = sum(nums)
    dp = [[-1 for i in range(s+1)] for y in range(len(nums))]
    def dfs(currentSum,index,otherSum):
        if index == len(nums):
            return abs(currentSum-otherSum)
        if dp[index][currentSum] == -1:
            dp[index][currentSum] = min(dfs(currentSum+nums[index],index+1,otherSum),dfs(currentSum,index+1,otherSum+nums[index]))
        return dp[index][currentSum]
    dfs(0,0,0)
    return dp[0][0]
print("Can partition: " + str(minSumDifference_topDown([1, 2, 3, 9])))
print("Can partition: " + str(minSumDifference_topDown([1, 2, 7, 1, 5])))
print("Can partition: " + str(minSumDifference_topDown([1, 3, 100, 4])))
    
