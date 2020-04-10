#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:31:55 2020

@author: huynguyen
"""
# 96. Unique Binary Search Trees

class Solution:
    def numTrees(self, n: int) -> int:
        array = [1,1,2,5]
        for i in range(4,n+1):
            v = 0
            for j in range(i):
                v+=array[j]*array[i-j-1]
            array.append(v)
        return array[n]