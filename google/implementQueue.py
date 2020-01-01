# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:49:21 2019

@author: huyn
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        arr = []
        while self.main:
            arr.append(self.main.pop())
        arr.append(x)
        for i in range(len(arr)-1,-1,-1):
            self.main.append(arr[i])

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.main.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.main[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.main)==0
        



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()