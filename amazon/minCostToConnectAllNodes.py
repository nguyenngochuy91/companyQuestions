# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:55:23 2019

@author: huyn
"""
"""
Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. 
The i-th edge connects nodes edges[i][0] and edges[i][1] together. 
Your task is to augment this set of edges with additional edges to connect all the nodes. 
Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.
Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 
and node 1 to node 6 at a minimum cost of 5 + 2 = 7."""
def minCostToRepairEdges(n,edges,newEdges):
    return