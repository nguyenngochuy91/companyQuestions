# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:24:34 2019

@author: Huy Nguyen
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
#Copy List with Random Pointer
def copyRandomList(head: 'Node') -> 'Node':
    dictionary = {}
    def dfs(head):
        if head:
            if head not in dictionary: #if we had not map this guy
                newLinkNode = Node(head.val,None,None)
                dictionary[head] = newLinkNode
                # we try to link our newLinkNode to the node that come next from head
                nextNode   = dfs(head.next)
                newLinkNode.next = nextNode# linking
                # we also try to link our newLinkNode to the random node lol
                nextRandomNode = dfs(head.random)
                newLinkNode.random = nextRandomNode
                return newLinkNode
            else:
                # if head already in, then we just return the copy of this head
                return dictionary[head]
        else:
            return None
    return dfs(head)
            