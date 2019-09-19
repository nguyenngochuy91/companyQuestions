# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:08:07 2019

@author: huyn
"""
from collections import deque
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
# 133. Clone Graph
#Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
#Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
def cloneGraphDFS(node):
    d = {}
    def dfs(node):
        if node:
            newNode = Node(node.val,[])
            d[node] = newNode
            for neighbor in node.neighbors:
                if neighbor not in d:
                    newNeighbor = dfs(neighbor)
                    d[neighbor]= newNeighbor
                    newNode.neighbors.append(newNeighbor)
                else:
                    newNode.neighbors.append(d[neighbor])
            return newNode
    newNode = dfs(node)
    return newNode
    

def cloneGraphLoop(node):
    queue = deque()
    visited = {}
    queue.append(node)
    visited[node] = Node(node.val, [])
    while queue:
        cur = queue.popleft()
        for neighbor in cur.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = Node(neighbor.val, [])
            visited[cur].neighbors.append(visited[neighbor])
    return visited[node]