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

class CodecBFS:
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

#a= TreeNode(1)
#b=TreeNode(2)
#c= TreeNode(3)
#d= TreeNode(4)
#e = TreeNode(5)
#f= TreeNode(6)
#g = TreeNode(7)
#a.left = b
#a.right = c
#b.left = d
#b.right = e
#e.left = f
#e.right= g
#serialize = CodecBFS()
#data=serialize.serialize(a)
#root = serialize.deserialize(data)

class CodecPreorder:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        myList =[]
        def dfs(root):
            if root:
                myList.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                myList.append("#")
        dfs(root)
        return ",".join(myList)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= data.split(",")
#        print (data)
        def dfs(data,index):
            if data[index]=="#":
                return None,1
            else:
                val = int(data[index])
                newNode = TreeNode(val)
                left,countL    = dfs(data,index+1)
                right,countR   = dfs(data,index+countL+1)
                newNode.left   = left
                newNode.right  = right
                return newNode,countL+countR+1
        return dfs(data,0)[0]
    def deserializeIterator(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= data.split(",")
#        print (data)
        def dfs(iterator):
            val=next(iterator)
            if val=="#":
                return None
            else:
                val = int(val)
                newNode = TreeNode(val)
                newNode.left= dfs(iterator)
                newNode.right= dfs(iterator)
                return newNode
        return dfs(iter(data))     
#a= TreeNode(1)
#b=TreeNode(2)
#c= TreeNode(3)
#d= TreeNode(4)
#e = TreeNode(5)
#f= TreeNode(6)
#g = TreeNode(7)
#a.left = b
#a.right = c
#b.left = d
#b.right = e
#e.left = f
#e.right= g
#serialize = CodecPreorder()
#data=serialize.serialize(a)
#root = serialize.deserializeIterator(data)
        
    
#Approach 1C: DFS preorder with non-NULL number of children info
        
class CodecNotNull:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        myList =[]
        def dfs(root):
            if root:
                myList.append(str(root.val))
                num  = 0
                if root.left:
                    num+=1
                if root.right:
                    num+=1
                myList.append(str(num))
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return ",".join(myList)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= data.split(",")
#        print (data)
        def dfs(data,index):
            nodeVal  = int(data[index])
            numChild = int(data[index+1])
            newNode = TreeNode(nodeVal)
            leftNum,rightNum =0,0
#            print (index,leftNum,rightNum)
            if numChild>=1:    
                newNode.left,leftNum    = dfs(data,index+2)
            if numChild==2:
                newNode.right,rightNum   = dfs(data,index+2+leftNum)
#            print (index,leftNum,rightNum)
            return newNode,leftNum+rightNum
        return dfs(data,0)[0]
    def deserializeIterator(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= data.split(",")
#        print (data)
        def dfs(iterator):
            try:
                nodeVal  = int(next(iterator))
                numChild = int(next(iterator))
                newNode = TreeNode(nodeVal)
                if numChild>=1:    
                    newNode.left    = dfs(iterator)
                if numChild==2:
                    newNode.right   = dfs(iterator)
                return newNode
            except:
                return None
        return dfs(iter(data))
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
serialize = CodecNotNull()
data=serialize.serialize(a)
root = serialize.deserialize(data)
#print (serialize.serialize(root) ==data)