# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:43:32 2019

@author: huyn
"""
"""
Distance Between Nodes in BST
Given a list of unique integers nums, construct a BST from it (you need to insert 
nodes one-by-one with the given order to get the BST) and find the distance between 
two nodes node1 and node2. Distance is the number of edges between two nodes. If any 
of the given nodes does not appear in the BST, return -1.

Input: nums = [2, 1, 3], node1 = 1, node2 = 3
Output: 2
Explanation:
     2
   /   \
  1     3
  
"""
class TreeNode:
    def __init__(self,val,left= None,right = None):
        self.val = val
        self.left = left 
        self.right = right

def distanceBetweenNode(root,node1,node2):
    maxVal,minVal = max(node1.val,node2.val), min(node1.val,node2.val)
    while True:
        if root.val<=maxVal and root.val>=minVal:
            break
        elif root.val < minVal:
            root = root.right
        else:
            root = root.left
    # we got out of the loop at the lowest common ancestor, now we find the distance by search the 2 node
    distance1 = search(root,node1)
    distance2 = search(root,node2)
    return distance1 + distance2
def search(root,node):
    d = 0
    while True:
        if root.val < node.val:
            root = root.right
        elif root.val > node.val:
            root = root.left
        else:
            return d
        d += 1
root = TreeNode(5)
a = TreeNode(2)
b = TreeNode(10)
c = TreeNode(1)
d= TreeNode(4)
e = TreeNode(12)
f = TreeNode(14)
root.left = a
root.right = b
a.left = c
a.right = d
b.left= e
b.right = f
print (distanceBetweenNode(root,c,a))