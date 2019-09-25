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
def maxPathSum(self,root: TreeNode) -> int:
    self.max = -float("inf")
    def dfs(node):
        if not node:
            return 0
        else:
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            
            throughNode = node.val+left+right
            self.max    = max(self.max,throughNode)
            return node.val+max(left,right)
    dfs(root)
    return self.max