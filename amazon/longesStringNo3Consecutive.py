# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:09:02 2019

@author: huyn
"""
"""
Longest string without 3 consecutive characters
Given A, B, C, find any string of maximum length that can be created such that no 
3 consecutive characters are same. There can be at max A 'a', B 'b' and C 'c'."""

import heapq
def buildString(A,B,C):
    string = ""
    queue = []
    # have aheap to keep count of best frequency
    if A:
        heapq.heappush(queue,[-A,"a"])
    if B:
        heapq.heappush(queue,[-B,"b"])    
    if C:
        heapq.heappush(queue,[-C,"c"])
    while queue:
        val,char = heapq.heappop(queue)
        if len(string)<2:
            string += char
            if val + 1!= 0:
                heapq.heappush(queue,[val+1,char])
        else:
            if string[-1] == string[-2]:
                lastChar = string[-1]
                if char!=lastChar:
                    string += char
                    if val + 1!= 0:
                        heapq.heappush(queue,[val+1,char])
                else:
                    # if queue is empty, break
                    if not queue:
                        break
                    # we will take the second best
                    val1, char1 = heapq.heappop(queue)
                    string += char1
                    heapq.heappush(queue,[val,char])
                    if val1 + 1 != 0:
                        heapq.heappush(queue,[val1+1,char1])
            else:
                string += char
                if val + 1!= 0:
                    heapq.heappush(queue,[val+1,char])
                        
    return string

#print (buildString(1,1,6))
#print (buildString(1,2,3))
#print (buildString(0,1,6))
#print (buildString(1,1,1))
#print (buildString(2,4,6))