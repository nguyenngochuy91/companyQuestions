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
def cloneGraphDFS(root):
    dictionary = {}
    def dfs(root):
        if root: 
            # time to create  a clone of root
            newNode = Node(root.val,[])
            dictionary[root] = newNode
            # for each neighbor ouf root
            for neighbor in root.neighbors:
                # create a clone, if neighbor was not traverse
                if neighbor not in dictionary:
                    cloneNeighbor = dfs(neighbor) # return the clone node
                # append this to our newNode neighbor
                else:
                    # alredy make a clone ,retrieve it
                    cloneNeighbor= dictionary[neighbor]
                newNode.neighbors.append(cloneNeighbor)
            return newNode
    return dfs(root)

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