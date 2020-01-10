#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 00:15:14 2020

@author: huynguyen
"""


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        def dfs(root):
            if root:
                if root in mapping:
                    return mapping[root]
                else:
                    newNeighbors = []
                    newNode = Node(root.val,newNeighbors)
                    mapping[root] = newNode
                    for neighbor in root.neighbors:
                        newNeighbor = dfs(neighbor)
                        newNeighbors.append(newNeighbor)
                    return newNode
            return None
        dfs(node)
        return mapping[node]