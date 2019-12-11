# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:48:08 2019

@author: huyn
"""

#ROD CUTTING
#Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way 
#that will maximize the profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.
def bruteForce(lengths,prices,rod):
    res = 0
    def dfs(currentIndex,currentLength,currentPrice):
        nonlocal res
        if currentLength <= rod:
            res = max(currentPrice,res)
            for i in range(currentIndex,len(lengths)):
                dfs(i,currentLength+lengths[i],currentPrice+prices[i])
    dfs(0,0,0)
    return res

#print(bruteForce([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

#def rod_cutting_topDown(lengths,prices,rod):
#    dp = [[-1 for i in range(len(rod+1))] for j in range(len(prices))]
#    def dfs(currentIndex,)
#    return