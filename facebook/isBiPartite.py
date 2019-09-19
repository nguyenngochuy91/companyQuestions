# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:31:52 2019

@author: Huy Nguyen
"""

#785. Is Graph Bipartite?
#Given an undirected graph, return true if and only if it is bipartite.
#
#Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every
# edge in the graph has one node in A and another node in B.
#
#The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.
#  Each node is an integer between 0 and graph.length - 1. 
# There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
def isBipartite(graph) -> bool:
    
    return

graph =[[1,3], [0,2], [1,3], [0,2]]
graph =[[1,2,3], [0,2], [0,1,3], [0,2]]