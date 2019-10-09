# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:34:49 2019

@author: huyn
"""
import random
#528. Random Pick with Weight
#Given an array w of positive integers, where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.
class randomlyWeight:

    def __init__(self, w):
        self.w= w
        for i in range(1,len(w)):
            self.w[i]+=self.w[i-1]
        self.max = w[-1]
    def pickIndex(self) -> int:
        num = random.randint(0,self.max)
        # binary search
        start,stop = 0, len(self.w)-1
        while start+1<stop:
            mid = (start+stop)//2
            if self.w[mid]<num:
                start = mid
            elif self.w[mid]>num:
                stop = mid
            else:
                return mid
        if self.w[start]>=num:
            return start
        if self.w[stop]>=num:
            return stop
        else:
            print (start,stop,num)

myWeights = randomlyWeight([1,3])
print (myWeights.pickIndex())