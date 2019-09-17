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
#426. Convert Binary Search Tree to Sorted Doubly Linked List
#Convert a BST to a sorted circular doubly-linked list in-place. Think of the left 
#and right pointers as synonymous to the previous and next pointers in a doubly-linked list.\
def treeToDoublyList(root: 'Node') -> 'Node':
    arr= []
    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)
            arr.append(root.val)
    if not arr:
        return None
    head = Node(arr[0],None,None)
    