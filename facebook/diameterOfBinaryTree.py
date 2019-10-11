# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:31:12 2019

@author: huyn
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#Diameter of Binary Tree
def diameterOfBinaryTree(root: TreeNode) -> int:
    myMax = [0]
    def dfs(root,myMax):
        if not root:
            return 0
        else:
            # at root, we look at the path from left, and path from right to see which one has the longer path
            left = dfs(root.left,myMax)
            right = dfs(root.right,myMax)
            currentLength = 1+left+right
            myMax[0] = max(myMax[0],currentLength)
            return 1+max(left,right)
    dfs(root,myMax)
    return max(myMax[0]-1,0)
a = TreeNode(1)
b = TreeNode(1)
c = TreeNode(1)
d = TreeNode(1)
e = TreeNode(1)
f = TreeNode(1)
g = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
f.right = g
#print (diameterOfBinaryTree(a))