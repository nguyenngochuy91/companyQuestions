# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:51:14 2020

@author: huyn
"""
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {}
        for i in range(n):
            d[i] = []
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count +=1
                queue = [i]
                while queue:
                    node = queue.pop()
                    for neighbor in d[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
        return count