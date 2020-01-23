#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:31:13 2020

@author: huynguyen
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split("\n")
        stack = []
        res = 0
        currentLength = 0 
        for item in input:
            item = item.split("\t")
     
            level = len(item)
            size = len(item[-1])
            while stack:
                lastLevel,lastSize = stack[-1]
                if lastLevel>= level: # means that we have to pop
                    currentLength -= lastSize+1
                    stack.pop()
                    
                else:
                    break
            # we add tje size to our currentLength
            currentLength += 1+size
            stack.append([level,size])
            if "." in item[-1]:
                res = max(res,currentLength)
        return max(0,res-1)