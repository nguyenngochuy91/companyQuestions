# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:33:05 2019

@author: huyn
"""
"""
Line of wines
There are N wines in a row. Each you you sell either the leftmost or the rightmost wine. 
The i-th wine has initial price p[i] and price k*p[i] in the k-th year. 
What is the maximum possible total profit
"""
# let dp[i][j] denote the best from index i to index j, we can figure the year from it as well
def lineOfWinesBottomUp(arr):
    size = len(arr)
    #dp[i][j] = max(Y*arr[i]+dp[i+1][j],Y*arr[j]+dp[i][j-1]
    # initialize dp[i][i] = p[i]*N
    # best score for the remaining interval from i to j
    return

def lineOfWinesTopdown(arr):
    size = len(arr)
    #dp[i][j-1] = max(dp[i][j-1], dp[i][j]+p[R]*Y)
    return