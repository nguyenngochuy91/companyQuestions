# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:27:37 2019

@author: huyn
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res= []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("n")
                continue
            else:
               
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
        return ",".join([str(i) for i in res])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= deque(data.split(","))
        if len(data)==1:
            if data[0]=="n":
                return None
        root = TreeNode(int(data.popleft()))
        head = root
        currentLevel = deque([head])
        while currentLevel:
            size = len(currentLevel)
            nextLevel = []
#            print (59,currentLevel,data,size)
            for i in range(size):
                node = currentLevel[i]
                left = data.popleft()
                right = data.popleft()
                if left !="n":
                    leftNode = TreeNode(int(left))
                    node.left = leftNode
                    nextLevel.append(leftNode)
                if right!="n":
                    rightNode = TreeNode(int(right))
                    node.right = rightNode
                    nextLevel.append(rightNode)
            currentLevel = nextLevel
        return root

a= TreeNode(1)
b=TreeNode(2)
c= TreeNode(3)
d= TreeNode(4)
e = TreeNode(5)
f= TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right= g
serialize = Codec()
data=serialize.serialize(a)
root = serialize.deserialize(data)