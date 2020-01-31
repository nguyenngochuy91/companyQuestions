# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:53:49 2020

@author: huyn
"""

#604. Design Compressed String Iterator
class StringIterator:

    def __init__(self, compressedString: str):
        self.string = []
        currentL = []
        count = 0
        for char in compressedString:
            if char.isalpha():
                if currentL:
                    self.string.append([currentL,count])
                    currentL = char
                    count = 0
                else:
                    currentL = char
                    count = 0
            else:
                count= count*10 +int(char)
        self.string.append([currentL,count])
        self.index = 0
        print (self.string)
    def next(self) -> str:
        res = " "
        if self.hasNext():
            string,count = self.string[self.index]
            res = string
            self.string[self.index][1]-=1
            if self.string[self.index][1] ==0:
                self.index+=1
        return res

    def hasNext(self) -> bool:
        return self.index<len(self.string)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()