# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:44:58 2019

@author: Huy Nguyen
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    return