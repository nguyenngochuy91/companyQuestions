# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:40:35 2020

@author: huyn
"""

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.stack = [i for i in range(combinationLength)]
        self.combinationLength = combinationLength
        self.size = len(characters)
        
    def next(self) -> str:
        if self.hasNext():
            res = [self.characters[index] for index in self.stack]
            count = 0
            while self.stack:
                item = self.stack.pop()
                if item+count+1<self.size:
                    self.stack.append(item+1)
                    break
                count+=1

            if self.stack:
                item = self.stack[-1]


            for i in range(count):
                item+=1
                self.stack.append(item)
            return "".join(res)
        

    def hasNext(self) -> bool:
        
        return self.stack[0]<=self.size-self.combinationLength




