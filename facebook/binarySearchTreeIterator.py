# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:38:25 2019

@author: Huy Nguyen
"""

#Tree Iterator
#173. Binary Search Tree Iterator   
#Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
#Calling next() will return the next smallest number in the BST.
# Definition for a binary tree node.\
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class ExtendedBSTIterator :

    def __init__(self, root: TreeNode,k):
        self.data= []
        self.head = TreeNode(None)
        def dfs(root):
            if root:
                dfs(root.left)
                self.data.append(root.val)
                dfs(root.right)
        dfs(root)
        self.index = -1
        self.lookBack =0 
        self.k = k

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.check = True
            self.index+=1
            self.lookBack = 0
            return self.data[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index<len(self.data)-1
    def hasPrev(self):
        return self.index>0 and self.lookBack<self.k
    def prev(self):
        if self.hasPrev():
            self.index-=1
            self.lookBack+=1
            return self.data[self.index]

#root = TreeNode(7)
#root.left = TreeNode(3)
#root.right = TreeNode(15,TreeNode(9),TreeNode(20))
#iterator   = ExtendedBSTIterator(root,3)
#print (iterator.head)
#print (iterator.head.right)
#print (iterator.head.left)
#print (iterator.hasNext())
#print (iterator.next())
#print (iterator.next())
#print (iterator.next())
#print (iterator.next())
#print (iterator.hasPrev())
#print (iterator.prev())
#print (iterator.hasPrev())
#print (iterator.prev())
#print (iterator.hasPrev())
#print (iterator.prev())
#print (iterator.hasPrev())
#print (iterator.prev())
#print (iterator.next())
#print (iterator.next())
#print (iterator.hasNext())
#print (iterator.hasPrev())
#print (iterator.prev())
#print (iterator.hasNext())
#print (iterator.next())
#next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.check = True
        self.head  = TreeNode(None)
        self.maxLast = None
        def dfs(root):
            if root:
                dfs(root.left)
                if not self.maxLast:
                    self.head.right = root
                else:
                    self.maxLast.right  = root
                    root.left = self.maxLast
                self.maxLast = root
                dfs(root.right)
        dfs(root)
#        print ()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.head = self.head.right
            return self.head.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.head.right:
            return True
        return False
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15,TreeNode(9),TreeNode(20))
iterator   = BSTIterator(root)
print (iterator.next())
print (iterator.next())
print (iterator.hasNext())
print (iterator.next())

print (iterator.hasNext())
print (iterator.next())

print (iterator.hasNext())
print (iterator.next())

print (iterator.hasNext())

