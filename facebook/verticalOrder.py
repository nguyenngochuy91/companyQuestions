# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:05:57 2019

@author: huyn
"""
from collections import deque
#314. Binary Tree Vertical Order Traversal
#Given a binary tree, return the vertical order traversal of its nodes' values. 
#(ie, from top to bottom, column by column).
#
#If two nodes are in the same row and column, the order should be from left to right.
class TreeNode(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
def verticalOrder(root):
    arr = {}
    queue = deque([(root,0)])
    while queue:
        node,level = queue.popleft()
        if node.left:
            queue.append([node.left,level-1])
        if node.right:
            queue.append([node.right,level+1])
        if level not in arr:
            arr[level]=[]
        arr[level].append(node.val)
    return [arr[i] for i in sorted(arr)]
