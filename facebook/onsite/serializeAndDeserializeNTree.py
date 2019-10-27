# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:02:03 2019

@author: huyn
"""

#428. Serialize and Deserialize N-ary Tree

# Definition for a Node.
from collections import deque
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
    def inorder(self):
        root = self
#        self.count = 10
        def traverse(root):
            if root:
                print (root.val)
#                self.count +=1
                for child in root.children:
                    traverse(child)

        traverse(root)
class CodecBFS:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # for this we have to  store how many children it contains
            if node:
                children = node.children
                res.append(node.val)
                res.append(len(children))
                # after each node, we will have number of children
                for child in children: # append this to our queue
                    queue.append(child)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            root = None
        else:
            data = deque(data)
            root = Node(data.popleft())
            head = root
            numChild = data.popleft()
            queue = deque([(head,numChild)])
            
            while queue:
#                print (queue)
                node, numChild = queue.popleft()
                temp = []
#                print (node.val,numChild)
                for i in range(numChild):
                    val = data.popleft()
                    num = data.popleft()
                    # create a child node
                    childNode = Node(val)
                    # append this child and its number of children to queue only if there are more children
                    if num:
                        queue.append((childNode,num))
                    # append this childNode to our node
                    temp.append(childNode)
                node.children = temp
        return root
        
root = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
#root.inorder()
codeBFS = CodecBFS()
data = codeBFS.serialize(root)
print (data)
newRoot = codeBFS.deserialize(data)
#newRoot.inorder()

print (codeBFS.serialize(newRoot))