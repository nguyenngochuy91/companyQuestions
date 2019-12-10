# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:50:13 2019

@author: huyn
"""
from typing import List
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value!=None:
            self.val = value
        else:
            self.val = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return type(self.val) == int
    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.val.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.val = value
    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger:
            return self.val
        return None
    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger:
            return None
        return self.val

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.depth = 0
        def getDepth(myList,depth):
            self.depth = max(self.depth,depth)
            for i in range(len(myList)):
                item = myList[i]
                if not item.isInteger():
                    getDepth(item.getList(),depth+1)
        getDepth(nestedList,1)
        self.depth+=1
        def dfs(myList,depth):
            s = 0
            for i in range(len(myList)):
                item = myList[i]
                if item.isInteger():
                    s += item.getInteger()*(self.depth-depth)
                else:
                    s += dfs(item.getList(),depth+1)
            return s
        return dfs(nestedList,1)