#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 06:24:37 2020

@author: huynguyen
"""

from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parents = {i:set() for i in range(numCourses)}
        children = {i:set() for i in range(numCourses)}
        for x,y in prerequisites:
            parents[x].add(y)
            children[y].add(x)
        start = deque([i for i in parents if len(parents[i]) == 0])

        while start:
            node = start.popleft()
            for child in children[node]:
                parents[child].remove(node)
                if len(parents[child])==0:
                    start.append(child)
        for i in parents:
            if len(parents[i])!=0:
                return False
        return True