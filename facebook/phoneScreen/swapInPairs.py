# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:57:50 2019

@author: Huy Nguyen
"""

def swapPairs(head) :
    if head and head.next:
        node = swapPairs(head.next.next)
        temp = head.next
        temp.next = head
        head.next = node
        head = temp
        return head
    elif head:
        return head
    else:
        return None
    