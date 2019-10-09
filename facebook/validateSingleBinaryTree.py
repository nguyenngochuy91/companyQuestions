# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:04:21 2019

@author: Huy Nguyen
"""

class TreeNode:
    def __init__(self,val):
        self.val =val
        self.left = None
        self.right = None

n1 =  TreeNode(1);
n2 =  TreeNode(2);
n3 =  TreeNode(3);
n4 =  TreeNode(4);
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n3
n3.left = n4
arr= [n1,n2,n3,n4]
#def isBinaryTree(arr):
    