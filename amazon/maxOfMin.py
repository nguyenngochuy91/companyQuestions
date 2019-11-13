# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:55:51 2019

@author: huyn
"""
"""
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] 
and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, 
the score of the path 8 → 4 → 5 → 9 is 4.

Don't include the first or final entry. You can only move either down or right at any point in time.
Input:
[[5, 1],
 [4, 5]]

Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.

Input:
[[1, 2, 3]
 [4, 5, 1]]

Output: 4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
Return the max of that, so 4."""
def maxOfMinPath(array):
    row = len(array)
    col = len(array[0])
    for c in range(2,col):
        array[0][c] = min(array[0][c-1],array[0][c])
    for r in range(2,row):
        array[r][0] = min(array[r-1][0],array[r][0])
    for r in range(1,row):
        for c in range(1,col):
            top = array[r-1][c]
            left = array[r][c-1]
            if r== row-1 and c== col-1:
                return max(top,left)
            else:
                array[r][c] = min(max(top,left),array[r][c])
array = [[5, 1],[4, 5]]
print (maxOfMinPath(array))
array = [[1, 2, 3],[4, 5, 1]]
print (maxOfMinPath(array))
 