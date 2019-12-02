# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 00:38:11 2019

@author: huyn
"""
"""
743. Network Delay Time
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, 
v is the target node, 
and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? 
If it is impossible, return -1.
"""

from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        d = {i+1:float("inf") for i in range(N)}
        graph = {i+1:{} for i in range(N)}
        d[K] = 0
        for u,v,w in times:
            graph[u][v] = w
        stack = [(0,K)]
        while stack:
            currentTime,currentNode = heapq.heappop(stack)
            for neighbor,time in graph[currentNode].items():
                if time+currentTime < d[neighbor]:
                    d[neighbor] = time + currentTime
                    heapq.heappush(stack,(time+currentTime,neighbor))
        m = max(d.values())
        if m == float("inf"):
            return -1
        return m