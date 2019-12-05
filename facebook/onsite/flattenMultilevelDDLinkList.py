# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:05:06 2019

@author: Huy Nguyen
"""
"""
430. Flatten a Multilevel Doubly Linked List
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, 
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own,
 and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list."""

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        childHead = self.flatten(head.child)
        nextHead  = self.flatten(head.next)
        if not nextHead:
            head.next = childHead
            head.child = None
        else: # means it has nextHead
            # it also has a child
            if childHead:
                # we need to link head -- child -- child.next -- .. .. --lastChild -- next
                nextTemp = nextHead
                lastChildHead= self.getLastNode(head.child)
                # link head next to childhead
                head.next = childHead
                childHead.prev = head
                # link lastCHild head next to nextHead
                lastChildHead.next = nextTemp
                nextTemp.prev = lastChildHead
                
            # if it does not have a child then just return head from the outer alredy
            
        return head
    def getLastNode(self,head):
        while head.next:
            head = head.next
        return head
    
