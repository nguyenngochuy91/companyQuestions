# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:21:41 2019

@author: huyn
"""

#297. Serialize and Deserialize Binary Tree
#Serialization is the process of converting a data structure or object into a sequence 
#of bits so that it can be stored in a file or memory buffer, or transmitted across a network 
#connection link to be reconstructed later in the same or another computer environment.
#
#Design an algorithm to serialize and deserialize a binary tree. There is no restriction on 
#how your serialization/deserialization algorithm should work. You just need to ensure that a 
#binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class CodecLevelOrder:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # if node None, append node
            if not node:
                res.append(None)
            else:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(data)
        if not data:
            root = None
        else:
            root = TreeNode(data.popleft())
            head = root
            queue = deque([head])
            while queue:
                node = queue.popleft()
                leftVal = data.popleft()
                rightVal = data.popleft()
                if leftVal:
                    nodeLeft = TreeNode(leftVal)
                    queue.append(nodeLeft)
                else:
                    nodeLeft = None
                if rightVal:
                    nodeRight = TreeNode(rightVal)
                    queue.append(nodeRight)
                else:
                    nodeRight = None
                node.left = nodeLeft
                node.right = nodeRight
        return root
        
class CodecPreorder:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def inorder(root):
            if root:
                res.append(root.val)
                inorder(root.left)
                inorder(root.right)
            else:
                res.append(None)
        inorder(root)
        return res
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        iterator = iter(data)
        def dfs(iterator):
            item = next(iterator,None)
            if not item:
                return None
            else:
            
                node = TreeNode(item)
                left = dfs(iterator)
                right = dfs(iterator)
                node.left = left
                node.right = right
                return node
        return dfs(iterator)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#root = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
#code = CodecLevelOrder()
#print (code.serialize(root))
#print (code.serialize(code.deserialize(code.serialize(root))))

root = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
code = CodecPreorder()
print (code.serialize(root))
print (code.serialize(code.deserialize(code.serialize(root))))