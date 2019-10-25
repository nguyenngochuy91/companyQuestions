
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:28:52 2019

@author: huyn
"""

#10. Regular Expression Matching
#
#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).

# T[i][j] =
# +T[i-1][j-1] if s[i]==p[j] or p[j]=="."
# +if pattern[j] == "*" :
#     - T[i][j-2] (not taking j-1 character in j, we care the boolean value 2 step back in pattern)
#     - T[i][j-1] if s[i] == p[j-1] or pattern [j-1] =="." 
# False

# Base case, 
def isMatch(s: str, p: str) -> bool:
    row = len(s)
    col = len(p)
    dp  = [[False]*(col+1) for i in range(row+1)] # accomodate the 0,0
    # base case matching non string to non string
    dp[0][0]= True
    for i in range(1,col+1):
        if p[i-1] == "*":
            dp[0][i] = dp[0][i-2]  # xa* depends on x match
    for i in range(1,row+1):
        for j in range(1,col+1):
            if s[i-1] == p[j-1] or p[j-1]==".":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1]=="*":
                dp[i][j] = dp[i][j-2] # this assign True if the previous already True
                if s[i-1] ==p[j-2] or p[j-2]==".":
                    dp[i][j] = dp[i-1][j] or dp[i][j] # if dp[i][j] was True already
            else:
                dp[i][j] = False
    print (dp)
    return dp[row][col]
s= "xaaby"
p = "xa*b.c"
print (isMatch(s,p))
# a.b -> T acb, axb,atb 
# a*b -> T b, aab, aaab , F acb, a,  
# a*b.*y -> T bzy,by,aabasdy, F ->
#      0 1 2 3 4 5 6
#        x a * b . c
# 0    T F F F F F F
# 1 x  F T F T F F F
# 2 a  F F T T F F F
# 3 a  F F F T 
# 4 b  F
# 5 y  F
