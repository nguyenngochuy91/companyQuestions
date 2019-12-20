# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 02:52:19 2019

@author: huyn
"""

#Longest Palindromic Subsequence
def findLongestSubsequence(string):
    def dfs(start,stop):
        if start >stop:
            return 0
        elif start == stop:
            return 1
        if string[start] == string[stop]:
            return 2+dfs(start+1,stop-1)
        else:
            return max(dfs(start+1,stop),dfs(start,stop-1))
    return dfs(0,len(string)-1)

#print(findLongestSubsequence("abdbca"))
#print(findLongestSubsequence("cddpd"))
#print(findLongestSubsequence("pqr"))

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
    return dp[0][len(s)-1]

print(findLongestSubsequenceTopDown("abdbca"))
print(findLongestSubsequenceTopDown("cddpd"))
print(findLongestSubsequenceTopDown("pqr"))