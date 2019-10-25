# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:08:25 2019

@author: Huy Nguyen
"""

#Given a singly linked list L: L0→L1→…→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
#You may not modify the values in the list's nodes, only nodes itself may be changed.
def reorderList( head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # count length
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    # if just have lest or equal to 2, everything stays the same
    if n < 3:
        return head
    # find head of and reverse second half
    first = second = head
    for _ in range((n + 1) // 2):
        second = second.next
    # reverse the second half into somehting like n->n-1>n-2...->n/2
    second = reverse(second)
    # merge
    for i in range(n // 2 - 1):
        # get the nexf both to link
        first_next, second_next = first.next, second.next
        # 1->2 ->3 ->4
        # 1->2 , 4->3
        # link 4 to 2
        second.next = first.next 
        # link 1 to 4
        first.next = second
        # we reset our first,second to be the head of 2,3
        first = first_next
        second = second_next
    # deal with last pair and possible last node
    last = None if n % 2 == 0 else first.next # we dont care about last if we have even node, else, it should be the first.next
    # 1->2->3
    # 5-> 4->3
    first.next = second # link 2->4 
    if last:
        # we have to set second next (4->3), and set last next to None 1->5->2->4->3
        second.next = last
        last.next = None

def reverse(head) :
    prev, cur = None, head
    while cur:
        next_ = cur.next
        cur.next = prev
        prev = cur
        cur = next_
    return prev