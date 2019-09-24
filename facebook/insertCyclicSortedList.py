# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:26:07 2019

@author: huyn
"""

#708. Insert into a Cyclic Sorted List
#Given a node from a cyclic linked list which is sorted in ascending order, write a
# function to insert a value into the list such that it remains a cyclic sorted list. 
# The given node can be a reference to any single node in the list, and may not be necessarily 
# the smallest value in the cyclic list.
#
#If there are multiple suitable places for insertion, you may choose any place to insert 
#the new value. After the insertion, the cyclic list should remain sorted.
#
#If the list is empty (i.e., given node is null), you should create a new single cyclic 
#list and return the reference to that single node. Otherwise, you should return the original given node.
#
#The following example may help you understand the problem better:
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
def insert(self, head: 'Node', insertVal: int) -> 'Node':
    root = head
    if not head:
        root = Node(insertVal)
        root.next = root
#    minVal  = float("inf")
#    minNode = None
#    maxVal  = -float("inf")
#    maxNode = Node
    # 3 cases
    #1 insertVal is less than min
    #2 insertVal is greater than max
    #3 insertVal <= max and insertVal >=min
    # 4 all node are equal, we wont hit differrent between min, max, therefore, have to insert anywhere
    else:
        head = head.next
        while True:

            if head.val<=insertVal : # head<val
                if head.next.val>=insertVal:# 3 cases, done
                    newNode = Node(insertVal)
                    newNode.next = head.next
                    head.next    = newNode
   
                    break
                else:
                    # so far looks like second case, we can check if head less than head.next, it means we have a min and max
                    #head.next <val
                    if head.val>head.next.val: # we hit max, and min
                        newNode = Node(insertVal)
                        newNode.next = head.next
                        head.next    = newNode
              
                        break
                    else:
                        head = head.next
            else: # val <head
                if head.next.val>=head.val:
                    head = head.next # we are in the increasing, wait until we hit the min
                else:
                    if insertVal<head.next.val:
                        # head.val >head.next.val , we hit a max , min
                        newNode = Node(insertVal)
                        newNode.next = head.next
                        head.next    = newNode
                        break  
                    else:
                        head= head.next
            # run this until we hit root again, this means, we have to insert our insertVal
            if head == root:
                newNode = Node(insertVal)
                newNode.next = head.next
                head.next    = newNode   

                break
    return root