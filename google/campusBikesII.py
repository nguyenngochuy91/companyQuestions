# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:27:35 2020

@author: huyn
"""

from typing import List
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        graph = {}
        for i in range(len(workers)):
            worker = workers[i]
            graph[i] = {}
            for j in range(len(bikes)):
                bike = bikes[j]
                distance = (worker[0]-bike[0])**2 + (worker[1] - biker[1])**2
                graph[i][j] = distance
        