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
#426. Convert Binary Search Tree to Sorted Doubly Linked List
#Convert a BST to a sorted circular doubly-linked list in-place. Think of the left 
#and right pointers as synonymous to the previous and next pointers in a doubly-linked list.\
minNode = None
maxNode = None
def treeToDoublyList(root: 'Node') -> 'Node':
    if not root:
        return None
    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)
            if not root.left and not root.right:
                root.min = root
                root.max = root
            elif root.left and root.right:
                leftMax,leftMin = root.left.max,root.left.min
                rightMax,rightMin = root.right.max,root.right.min
                root.left = leftMax
                leftMax.right = root
                root.right = rightMin
                rightMin.left = root
                root.min = leftMin
                root.max = rightMax
            elif root.left:
                leftMax,leftMin = root.left.max,root.left.min
                leftMax.right= root
                root.left = leftMax
                root.min = leftMin
                root.max = root
            else:
                rightMax,rightMin = root.right.max,root.right.min
                root.right = rightMin
                rightMin.left = root
                root.min=root
                root.max =rightMax
            # logic for root
    dfs(root)
treeToDoublyList(A)
    
    