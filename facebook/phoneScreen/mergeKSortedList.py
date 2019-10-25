# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:29:05 2019

@author: huyn
"""
from typing import List
import heapq
#23. Merge k Sorted Lists
#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeKListsV1(self, lists: List[ListNode]) -> ListNode:
    root = ListNode(0) # this is our root
    head = root
    while True:
        currentMin = float("inf")
        i          = None
        for index in range(len(lists)):
            currentNode = lists[index]
            if currentNode:
                val = currentNode.val
                if val <currentMin:
                    val = currentMin
                    i   = index # store this so we can do node.next
        if i == None: # this means we have gone through all the node
            break
        else:
            # create new node
            newNode   = ListNode(currentMin)
            head.next = newNode
            head      = head.next
            # make the node at array index i become next
            lists[i]  = lists[i].next
                
    return root.next

def mergeKListsV2(self, lists: List[ListNode]) -> ListNode:
    h = [(l.val, idx) for idx, l in enumerate(lists) if l]
    heapq.heapify(h) # make it a mean heap by  value
    head = cur = ListNode(None)
    while h:
        val, idx = heapq.heappop(h)
        cur.next = ListNode(val)
        cur = cur.next
        node = lists[idx] = lists[idx].next
        if node:
            heapq.heappush(h, (node.val, idx))
    return head.next