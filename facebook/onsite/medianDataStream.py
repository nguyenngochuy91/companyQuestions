# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:54:02 2019

@author: huyn
"""
"""
295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far."""
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # top that is a min heap that store min from upper half
        self.top = []
        # bot that is a max heap store max from bottom half
        self.bot = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.top and not self.bot:
            heapq.heappush(self.top,num)
        elif not self.bot:
            # we have something in self top, but not self bot, basically we have 2 elemtns so far
            num1 = heapq.heappop(self.top)
            num2 = num
            if num1 > num2:
                heapq.heappush(self.bot,-num2)
                heapq.heappush(self.top,num1)
            else:
                heapq.heappush(self.bot,-num1)
                heapq.heappush(self.top,num2)
        else:
            minTop = self.top[0]
            maxBot = -self.bot[0]
            if num <= minTop and num >= maxBot:
                if len(self.top) < len(self.bot):
                    heapq.heappush(self.top,num)
                elif len(self.bot) < len(self.top):
                    heapq.heappush(self.bot,-num)
                else:
                    heapq.heappush(self.top,num)
            elif num >minTop:
                if len(self.top)<=len(self.bot):
                    heapq.heappush(self.top,num)
                else: # if top > bot, pop the minTop, add it to Bot
                    heapq.heappush(self.bot,-heapq.heappop(self.top))
                    heapq.heappush(self.top,num)
            else: # num < maxBot
                if len(self.bot) <=len(self.top):
                    heapq.heappush(self.bot,-num)
                else:
                    heapq.heappush(self.top,-heapq.heappop(self.bot))
                    heapq.heappush(self.bot,-num)
        #print (self.top,self.bot)
    def findMedian(self):
        """
        :rtype: float
        """
        #print ("median",self.top,self.bot)
        if len(self.top) == len(self.bot):
            minTop = self.top[0]
            maxBot = -self.bot[0]
            return (minTop+maxBot)/2
        elif len(self.top) < len(self.bot):      
            return -self.bot[0]
        else:
            return self.top[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()