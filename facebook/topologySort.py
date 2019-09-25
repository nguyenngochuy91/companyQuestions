# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:00:52 2019

@author: huyn
"""
from collections import deque
#topology sorting
class Node:
    def __init__(self,val,neighbor=[]):
        self.val       = val
        self.neighbors = neighbor
def topologySort(nodes):
    res = []
    # go through the dictionary, find the parent for all the node
    parentNodeOf = {}
    for node in nodes:
        if node not in parentNodeOf:
            parentNodeOf[node] = set()
        for neighbor in node.neighbors:
            if neighbor not in parentNodeOf:
                parentNodeOf[neighbor] = set()
            parentNodeOf[neighbor].add(node)
    # list of node without incoming edges
#    print ("parentNodeOf",parentNodeOf)
    startNode =[node for node in parentNodeOf if len(parentNodeOf[node])==0]
#    print (startNode)
    while startNode:
        node = startNode.pop()
        res.append(node)
        for neighbor in node.neighbors:
            # remove the parent node from this neighbor
            parentNodeOf[neighbor].remove(node)
            if not parentNodeOf[neighbor]: # if no more, then this becamses a start node
                startNode.append(neighbor)
    return [item.val for item in res]

a= Node(5)
b= Node(7)
c= Node(3)
d= Node(11)
e= Node(8)
f= Node(2)
g= Node(9)
h= Node(10)
a.neighbors= [d]
b.neighbors=[d,e]
c.neighbors=[e,h]
d.neighbors=[f,g,h]
e.neighbors=[g]
nodes = [a,b,c,d,e,f,g,h]
res = topologySort(nodes)
