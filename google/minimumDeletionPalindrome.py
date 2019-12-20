# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:10:39 2019

@author: Huy Nguyen
"""

#Minimum deletion to make palindromic
# convert this to maximum length subsequence
def findLongestSubsequenceTopDown(s):
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    def dfs(start,stop):
        if start >stop:
            return 0
        elif start == stop:
            return 1
        if s[start] == s[stop]:
            dp[start][stop] = 2 + dfs(start+1,stop-1)
        else:
            dp[start][stop] = max(dfs(start+1,stop),dfs(start,stop-1))
        return dp[start][stop]
    dfs(0,len(s)-1)
    return len(s)-dp[0][len(s)-1]