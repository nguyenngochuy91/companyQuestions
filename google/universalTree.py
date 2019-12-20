# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:20:05 2019

@author: huyn
"""

class Tree:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right
#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
#Given the root to a binary tree, count the number of unival subtrees.
def countUniversal(node):
    count = 0
    def isUniversal(node):
        nonlocal count
        if node:
            check = False
            if node.left and node.right:
                isLeft = isUniversal(node.left)
                isRight = isUniversal(node.right)
                if isLeft and isRight and node.left.val == node.right.val == node.val:
                    check = True
            elif node.left:
                isLeft = isUniversal(node.left)
                if isLeft and node.left.val == node.val:
                    check = True
            elif node.right:
                isRight = isUniversal(node.right)
                if isRight and node.right.val == node.val:
                    check = True
            else:
                check = True
            return check
    isUniversal(node)
    return count
