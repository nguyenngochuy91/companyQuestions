# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:06:23 2019

@author: huyn
"""
"""
Critical Routers
AWS wants to increase the reliability of their network by upgrading crucial data center routers. 
Each data center has a single router that is connected to every other data center through a direct link or 
some other data center.

To increase the fault tolerance of the network, AWS wants to identify routers which would result in a 
disconnected network if they went down and replace then with upgraded versions.

Write an algorithm to identify all such routers.

Input:

The input to the function/method consists of three arguments:

numRouters, an integer representing the number of routers in the data center.
numLinks, an integer representing the number of links between the pair of routers.
Links, the list of pair of integers - A, B representing a link between the routers A and B. The network will be connected."""
from collections import deque
# O(n^2)
def singlePointOfFailure(connections,n,numLinks):
    n = len(connections)
    d = {i:[] for i in range(n)}
    for x,y in connections:
        d[x].append(y)
        d[y].append(x)
    res = []
    for failRouter in range(n):
        queue = deque([failRouter+1] if failRouter+1<n else [0])
        visited = set()
        visited.add(queue[0])
        while queue:
            for i in range(len(queue)):
                currentRouter = queue.popleft()
                for neighbor in d[currentRouter]:
                    if neighbor not in visited and neighbor!= failRouter:
                        queue.append(neighbor)
                        visited.add(neighbor)
        if len(visited)!=n-1:
            res.append(failRouter)
    return res

def dfs(connections,n,numLinks):
    return
connections = [[1, 3], [3, 4], [1, 4], [4, 5]]
print (singlePointOfFailure(connections,5,4))