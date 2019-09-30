# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:40:26 2019

@author: Huy Nguyen
"""

#Sorted Iterator
#ou have three unsorted list of numbers. Design/Write function that will return next minimum element out of these lists (remove that element from list).
list1 = [5, 1, 2, 4]
list2 = [4, 6, 3]
list3 = [9, 0, 7]
import heapq
class Iterator:
    def __init__(self,lists):
        self.lists = lists
        self.heap  = []
        for index,eachList in enumerate(self.lists):
            eachList.sort(reverse= True)
            heapq.heappush(self.heap,(eachList.pop(),index))
    def next(self):
        if self.heap:
            val,index= heapq.heappop(self.heap)
            if self.lists[index]:
                heapq.heappush(self.heap,(self.lists[index].pop(),index))
            return val

iterator = Iterator([list1,list2,list3])
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())
print (iterator.next())