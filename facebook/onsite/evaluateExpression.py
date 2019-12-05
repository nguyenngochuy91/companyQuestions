# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 07:27:58 2019

@author: Huy Nguyen
"""
"""
Given two expression in the form of a binary tree, find if both the expressions are equivalent.
exp1 = a + b + c + a
exp2 = a + a + b + c

     +
    / \
   +   +
  / \ / \
  a b c a

     +
    / \
   +   +
  / \ / \
  a a b c"""
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class evaluatePlusMinus:
    def __init__(self,root):
        return
    
