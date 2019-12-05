# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:54:04 2019

@author: Huy Nguyen
"""
"""
closes value in binary search tree 
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.min,self.res = float("inf"),None
        def inorder(root,target):
            if root:
                inorder(root.left,target)
                if root.val>=target:
                    if self.res==None:
                        self.res = root.val
                        self.min = abs(root.val-target)
                        return
                    else:
                        val =root.val-target
                        if val<self.min:
                            self.res = root.val
                        return
                else:
                    self.min = abs(root.val-target)
                    self.res = root.val
                inorder(root.right,target)
        inorder(root,target)
        return self.res