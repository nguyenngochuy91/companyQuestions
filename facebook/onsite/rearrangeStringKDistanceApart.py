# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 03:37:04 2019

@author: Huy Nguyen
"""
"""
358. Rearrange String k Distance Apart
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string ""."""
import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if len(s) == 1 or k==0:
            return s
        string = ""
        d = {}
        for letter in s:
            if letter not in d:
                d[letter] = 0
            d[letter] += 1
        queue = []
        for letter in d:
            heapq.heappush(queue,[-d[letter],letter])
        while queue:
            stringUsed = []
            for i in range(min(k,len(queue))):
                val,item = heapq.heappop(queue)
                stringUsed.append([item,val])
       
            if len(stringUsed)<k and check(stringUsed):
                return ""
            for item,val in stringUsed:
                if val+1<0:
                    heapq.heappush(queue,[val+1,item])
                string += item
          
        return string
def check(string):
    for item,val in string:
        if val+1!=0:
            return True
    return False