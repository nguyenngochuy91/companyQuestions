# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:54:44 2019

@author: huyn
"""

#449. Serialize and Deserialize BST
#Serialization is the process of converting a data structure or object into a sequence 
#of bits so that it can be stored in a file or memory buffer, or transmitted across a network 
#connection link to be reconstructed later in the same or another computer environment.
#
#Design an algorithm to serialize and deserialize a binary search tree. There is no restriction 
#on how your serialization/deserialization algorithm should work. You just need to ensure that a 
#binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
#The encoded string should be as compact as possible.
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
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))