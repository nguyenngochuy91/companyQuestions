# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        d= {i:[] for i in range(len(arr))}
        for index,val in enumerate(arr):
            index1 = index+val
            index2 = index-val
            if index1>=0 and index1<len(arr):
                d[index].append(index1)
            if index2>=0 and index2<len(arr):
                d[index].append(index2)
        visited = [False]*len(arr)
        visited[start]= True
        stack = [start]
        while stack:
            index = stack.pop()
            if arr[index] == 0:
                return True
            for neighbor in d[index]:
                if not visited[neighbor]: 
                    visited[neighbor] = True
                    stack.append(neighbor)
        return False