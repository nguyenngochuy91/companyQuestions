# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:36:03 2019

@author: Huy Nguyen
"""
#Read N Characters Given Read4 II
class Solution:
    def __init__(self):
        self.data =[] # this store extra info that read4 reads and our read did not need that much of data
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        smallBuf = [""]*4
        # firstly, since we might have some left overdata from previous read4 stored in data, we retrieve until either our self.data is empty or we fill n of buff
        # create a flag to check whether we have use our data
        usedData = False # this served as sometimes we only go through the loop once which makes i=0, but we actually need to make it 1
        for i in range(min(n,len(self.data))):
            buf[i] = self.data[i]
            n-=1
            usedData = True
        if usedData:
            i+=1
        else:
            i= 0
        # we remove the amount that used from data
        self.data = self.data[i:]
        while n>0:
            size = read4(smallBuf)
            if size ==0: # dont have any more in input stream, we are done
                break
            for index in range(min(size,n)):
                buf[i]=smallBuf[index]
                i+=1
                n-=1
            # might be a case where our read4 is greater, means we read4 more than we need for read
            # store it in our self.data
            for j in range(index+1,size):
                self.data.append(smallBuf[j])
        return i