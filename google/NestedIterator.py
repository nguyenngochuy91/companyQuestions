# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:30:36 2019

@author: huyn
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.index      = 0
        self.temp = None
    def next(self):
        """
        :rtype: int
        """
        if self.temp==None:
            
            currentItem = self.nestedList[self.index]
#            print (currentItem)
            if type(currentItem)!=list:
                self.index += 1
                return currentItem
            else:
                self.temp = NestedIterator(currentItem)
                return self.temp.next()
        else:
            if self.temp.index < len(self.temp.nestedList):
                return self.temp.next()
            else:
                self.temp = None
                self.index += 1
                if self.index<len(self.nestedList):
                    return self.next()
                
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.temp == None:
            return self.index < len(self.nestedList)
        else:
#            print ("inner:{}, outer:{}".format(self.temp.index,self.index))
            return self.temp.index< len(self.temp.nestedList) or self.index < len(self.nestedList)
nestedList = [[1,1],[3,4,[6,7,[8,9]]]]
iterator = NestedIterator(nestedList)
while iterator.hasNext():
#    print (50,iterator.temp,iterator.index)
    print (iterator.next())