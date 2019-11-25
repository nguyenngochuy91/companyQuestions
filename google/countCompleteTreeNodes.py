# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:50:21 2019

@author: huyn
"""
"""
Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.
In a complete binary tree every level, except possibly the last, is completely filled, and 
all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0