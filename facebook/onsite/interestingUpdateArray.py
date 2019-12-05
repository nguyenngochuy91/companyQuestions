# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:48:16 2019

@author: Huy Nguyen
"""
"""
Given an array of elements. We have 3 functions -
get(index) - return value at given index
set(index, val) - set value at given index
setAllElements(val) -  set all elements as the given value"""
class Array:
    def __init__(self,arr):
        self.arr = arr
        self.updatedAfterSwap = set()
        self.val = None
    def set(self,index,val):
        self.arr[index] = val
        self.updatedAfterSwap.add(index)
    def get(self,index):
        if self.val== None or index in self.updatedAfterSwap:
            return self.arr[index]
        return self.val
    def setAllElements(self,val):
        self.val = val
        self.updatedAfterSwap= set()