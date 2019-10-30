# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:15:08 2019

@author: Huy Nguyen
"""
"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list."""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = ListNode(0)
        root.next = head
        count =0
#        while count + 1<m:# try to get to the head rightbefore the node
            
        return root.next