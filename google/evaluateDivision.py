# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:55:33 2019

@author: huyn
"""

#Evaluate Division
#Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
#Given some queries, return the answers. If the answer does not exist, return -1.0.
#
#Example:
#Given a / b = 2.0, b / c = 3.0.
#queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
#return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
#The input is: vector<pair<string, string>> equations, vector<double>& values, 
#vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. 
#This represents the equations. Return vector<double>.
from typing import List
from collections import deque
def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = {}
    for i in range(len(equations)):
        x,y = equations[i]
        value = values[i]
        if x not in graph:
            graph[x] = {}
        if y not in graph:
            graph[y] = {}
        graph[x][y] = value
        graph[x][x] = 1.0
        graph[y][y] = 1.0
        graph[y][x] = 1/value

    res = []
    for x,y in queries:
        queue = []
        visited = set([x])
        if x not in graph:
            res.append(-1.0)
            continue
        for neighbor in graph[x]:
            queue.append([neighbor,graph[x][neighbor]])
            visited.add(neighbor)
        queue = deque(queue)
        found = False
        while queue:
            size = len(queue)
            for i in range(size):
                node,val = queue.popleft()
                if node == y:
                    res.append(val)
                    found = True
                    break
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        nextVal = graph[node][neighbor]
                        queue.append([neighbor,val*nextVal])
        if not found:
            res.append(-1.0)

    return res