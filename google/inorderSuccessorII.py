# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:45:36 2020

@author: huyn
"""

#510. Inorder Successor in BST II

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        self.found = False
        self.res = None
        root = node
        while root.parent:
            root = root.parent
        def dfs(root):
            if root:
                dfs(root.left)
                if root == node:
                    self.found = True
                else:
                    if self.found and self.res == None:
                        self.res = root
                        return 
                dfs(root.right)
        dfs(root)
        return self.res
        
    def inorderSuccessor2(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent