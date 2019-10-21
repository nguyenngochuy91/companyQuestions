# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:33:23 2019

@author: huyn
"""

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dum = ListNode(0)
    dum.next = head
    last = head
    for i in range(n):
        last = last.next
    if not last:
        return dum.next.next
    while last.next:
        head = head.next
        last = last.next
    head.next = head.next.next
    return dum.next
