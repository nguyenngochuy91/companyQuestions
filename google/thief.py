# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 02:40:47 2019

@author: huyn
"""

#House thief
def findMax(array):
    def dfs(index,currentSum):
        if index>=len(array):
            return currentSum
        else:
            val = array[index]
            first = dfs(index+1,currentSum)
            second = dfs(index+2,currentSum+val)
            return max(first,second)
            
    return dfs(0,0)
#print(findMax([2, 5, 1, 3, 6, 2, 4]))
#print(findMax([2, 10, 14, 8, 1]))

def findMaxDP(array):
    dp = [0]*len(array)
    def dfs(index):
        if index<len(array):
            if dp[index]==0:
                dp[index] = max(array[index]+dfs(index+2),dfs(index+1))
            return dp[index]
        else:
            return 0
    dfs(0)
    return dp[0]
print(findMaxDP([2, 5, 1, 3, 6, 2, 4]))
print(findMaxDP([2, 10, 14, 8, 1]))