# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:18:04 2019

@author: huyn
"""

#124. Binary Tree Maximum Path Sum
#Given a non-empty binary tree, find the maximum path sum.
#
#For this problem, a path is defined as any sequence of nodes from some starting
#node to any node in the tree along the parent-child connections. The path must 
#contain at least one node and does not need to go through the root.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def maxPathSum(self, root: TreeNode) -> int:
    
    return