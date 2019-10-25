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

# a graph is biPartite if
# we can split it into 2 set(or 2 color code) 
def isBipartite(graph):
    d = {}
    # idea is we break our graph into graph that is connected
    # then try to 2 color them
    for node,neighbors in enumerate(graph):
        if node not in d: # have not assign this node, that means any of the edge was not assigned neither
        # we intiate a new stack for this node, preferably keep traversing the stack until stack is done
            stack = [node]
            d[node] = 0 
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in d:
                        # we will explore this node
                        stack.append(neighbor)
                        d[neighbor]= 1-d[node]
                    elif d[neighbor]==d[node]: 
                    # have a clashing if we hit a node with same colore (basically a triangle)
                        return False
    return True

graph = [[3],[2,4],[1],[0,4],[1,3]]
print (isBipartite(graph))
#graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
#print (isBipartite(graph))