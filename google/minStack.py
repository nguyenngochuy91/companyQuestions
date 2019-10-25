# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:08:19 2019

@author: huyn
"""

#Min Stack
#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min   = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min:
            last = self.min[-1]
            if last < x:
                self.min.append(last)
            else:
                self.min.append(x)
        else:
            self.min.append(x)
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]