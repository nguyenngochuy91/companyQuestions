#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:36:29 2020

@author: huynguyen
"""


# 518. Coin Change 2
# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d = {}
        def dfs(target,index):
            if (target,index) in d:
                return d[(target,index)]
            else:
                if target == 0:
                    return 1
                elif index == -1:
                    return 0
                else:
                    index = findIndex(coins,target,index)
                    d[(target,index)] = 0
                    if index!=-1:
                        d[(target,index)] += dfs(target,index-1)
                        d[(target,index)] += dfs(target-coins[index],index)
                    return d[(target,index)]
        return dfs(amount,len(coins)-1)
def findIndex(array,target,currentIndex):
    if array[currentIndex]<=target:
        return currentIndex
    start = 0
    stop = currentIndex
    while start+1<stop:
        mid = (start+stop)//2
        if array[mid]>target:
            stop = mid
        else:
            start = mid
    if array[stop] <=target:
        return stop
    if array[start] <=target:
        return start
    return -1
                