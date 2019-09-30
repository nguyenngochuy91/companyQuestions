# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:17:19 2019

@author: huyn
"""
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
A= Node(4,None,None)
B= Node(5,None,None)
C= Node(2,None,None)
D= Node(1,None,None)
E= Node(3,None,None)
A.left = C
A.right = B
C.left = D
C.right= E
#426.     
#Convert a BST to a sorted circular doubly-linked list in-place. Think of the left 
#and right pointers as synonymous to the previous and next pointers in a doubly-linked list.\
minNode = None
maxNode = None
def treeToDoublyList(self,root: 'Node') -> 'Node':
    if not root:
        return None
    self.min,self.max = None,None
    def dfs(root):
        if root:
            dfs(root.left)
            # logic for root
            if not self.max: # means that we hit the first root with val value, and we did not store our self.max as the last node yet, therefore, it is minimum
                self.min = root
            else:
                # already have the last max, we can point it to our node, and node.left to max
                root.left =self.max
                self.max.right = root
            # set our root to our max now
            self.max = root
            dfs(root.right)
    dfs(root)
    self.min.left = self.max
    self.max.right= self.min
    return root
treeToDoublyList(A)
    
    