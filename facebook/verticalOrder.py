# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:05:57 2019

@author: huyn
"""

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
    arr = []
    return arr