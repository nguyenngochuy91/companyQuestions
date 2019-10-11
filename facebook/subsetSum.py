# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:45:59 2019

@author: huyn
"""

def subsetSumDP(arr,K):
    row = len(arr)+1
    col = K+1
    dp =  [[False]*col for i in range(row)]
    for r in range(row):
        dp[r][0]=True
    for r in range(1,row):
        for c in range(1,col):
            dp[r][c] = dp[r-1][c] or dp[r-1][c-arr[r-1]]
    return dp[row-1][col-1]

arr = [4,5,0,2,3,1]
K = 5
#print (subsetSumDP(arr,K))

def subsetSumBacktrack(arr,K):
    arr.sort()
    def dfs(accumulate,index,currentPath,K):
        if accumulate == K:
            print (currentPath)
        elif accumulate<K and index<len(arr):
            val = accumulate+arr[index]
            if val<=K:
                currentPath.append(arr[index])
                dfs(val,index+1,currentPath,K)
                currentPath.pop()
                dfs(accumulate,index+1,currentPath,K)
    dfs(arr[0],1,[arr[0]],K)
    dfs(0,1,[],K)
    return
#subsetSumBacktrack(a