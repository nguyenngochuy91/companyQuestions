# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:49:18 2019

@author: huyn
"""
from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size = len(stones)
        graph = {i:[] for i in range(size)}
        cc = 0
        for i in range(size-1):
            for j in range(i+1,size):
                x1,y1 = stones[i]
                x2,y2= stones[j]
                if x1 == x2 or y1 == y2:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        def dfs(x):
            for nei in graph[x]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei) 
        for node in graph:
            if node not in visited:
                visited.add(node)
                dfs(node)
                cc +=1

        return size-cc