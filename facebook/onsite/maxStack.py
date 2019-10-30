# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:29:49 2019

@author: Huy Nguyen
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max   = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.max.append(x)
        else:
            self.stack.append(x)
            self.max.append(max(self.max[-1],x))
#        print (16,self.stack,self.max)
    def pop(self) -> int:
        self.max.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max[-1]

    def popMax(self) -> int:
        myMax = self.peekMax()
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] == myMax:
#                print ("found at:",i)
                self.stack.pop(i)
                for j in range(len(self.stack)-i+1):
                    self.max.pop()
#                    print ("pop max")
                for j in range(i,len(self.stack)):
                    if self.max:
                        self.max.append(max(self.max[-1],self.stack[j]))
                    else:
                        self.max.append(self.stack[j])
                break
#        print (41,self.stack,self.max)
        return myMax


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()