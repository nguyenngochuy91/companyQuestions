# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:28:16 2019

@author: huyn
"""

#Word Squares
#Given a set of words (without duplicates), find all word squares you can build from them.
#
#A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
#For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
from typing import List
def wordSquares(words: List[str]) -> List[List[str]]:
    res = [] 
    n = len(words[0])
    matrix = [[""]*n for i in range(n)]
    d = {}
    for word in words:
        for i in range(n):
            # we check if i is in d
            if i not in d:
                d[i] = {}
            prefix = word[:i]
            if prefix not in d[i]:
                d[i][prefix] = []
            suffix = word[i:]
            d[i][prefix].append(suffix)
#    print (d)
    def dfs(index,n):
        if index == n:
            temp = []
            for row in matrix:
                temp.append("".join(row))
            res.append(temp)
        elif index<n:
            # we look at our current row at index, and the prefix we have sofar
#            print (matrix)
            prefix = "".join(matrix[index])
            size = len(prefix)
            if prefix in d[size]:
                for potential in d[size][prefix]:
                    startRow,startCol = size,size
                    # we fill row and col of our matrix with this potential
                    for j in range(size,n):
                        matrix[startRow][j] = potential[j-size]
                        matrix[j][startCol] = potential[j-size]
                    dfs(index+1,n)
                    # we undo the filling part
                    for j in range(size,n):
                        matrix[startRow][j] = ""
                        matrix[j][startCol] = ""   
    dfs(0,n)      
    return res
    
words = ["area","lead","wall","lady","ball"]
print (wordSquares(words))