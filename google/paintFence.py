# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 01:38:06 2020

@author: huyn
"""
#276. Paint Fence
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n ==0:
            return 0
        if n==1:
            return k
        if k == 1 and n>2:
            return 0
        arr = [[1,0] for i in range(k)]
        for i in range(1,n):
            newArr = []
            noAdjacent = sum([item[0] for item in arr])
            adjacent = sum([item[1] for item in arr])
            for j in range(k):
                temp = [0,0]
                temp[0] = adjacent-arr[j][0]+noAdjacent- arr[j][1]
                temp[1] = arr[j][0]
                newArr.append(temp)
            arr = newArr
        noAdjacent = sum([item[0] for item in arr])
        adjacent = sum([item[1] for item in arr])        
        return noAdjacent+adjacent