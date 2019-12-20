# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:32:11 2019

@author: Huy Nguyen
"""

#Longest Palindromic Substring

def recursive(s):
    def dfs(start,stop):
        if start>stop:
            return 0
        elif start == stop:
            return 1
        else:
            if s[start] == s[stop]:
                length = stop-start-1
                if length == dfs(start+1,stop-1):
                    return 2+length
            return max(dfs(start+1,stop),dfs(start,stop-1))
    return dfs(0,len(s)-1)

def recursiveTopDown(s):
    dp = [[-1 for i in range(len(s))] for j in range(len(s))]
    def dfs(start,stop):
        if start>stop:
            return 0
        elif start == stop:
            return 1
        else:
            if dp[start][stop] == -1:
                if s[start] == s[stop]:
                    length = stop-start-1
                    if length == dfs(start+1,stop-1)    :
                        dp[start][stop] = 2+length
                        return dp[start][stop]
                dp[start][stop] = max(dfs(start+1,stop),dfs(start,stop-1))
            return dp[start][stop]
    dfs(0,len(s)-1)
    return dp[0][len(s)-1]
#print(recursiveTopDown("abdbca"))
#print(recursiveTopDown("cddpd"))
#print(recursiveTopDown("pqr"))