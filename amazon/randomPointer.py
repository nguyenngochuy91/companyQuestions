# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 00:26:35 2019

@author: huyn
"""
"""
138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dictionary = {}
        def dfs(node):
            if not node:
                return None
            if node in dictionary:
                return dictionary[node]
            else:
                newNode = Node(node.val)
                dictionary[node] = newNode
                nextNode = dfs(node.next)
                randomNode = dfs(node.random)
                newNode.next = nextNode
                newNode.random = randomNode
                return newNode
        return dfs(head)