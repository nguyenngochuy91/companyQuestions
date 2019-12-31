# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time,random
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count  = 0
        for num in nums:
            while num>=100:
                num//=100
            if num>=10:
                count+=1
        return count
    def findNumbers2(self, nums: List[int]) -> int:
        count  = 0
        for num in nums:
            length = getLength(num)+1
            if length%2==0:
                count+=1
        return count

def getLength(num):
    start = 0
    stop = 33
    while start +1 <stop:
        mid = (start+stop)//2
        if 10**mid>num:
            stop = mid
        else:
            start = mid
    return start
# arr = []
# for i in range(10000):
#     arr.append(10000000000000000000000000000000)
# solution = Solution()
# start = time.time()
# print (solution.findNumbers2(arr))
# stop = time.time()
# print ((stop-start))
# start = time.time()
# print (solution.findNumbers(arr))
# stop = time.time()
# print ((stop-start))


def abc():
    a= 0
    def cdf():
        nonlocal a
        a+=1
    cdf()
    print (a)
abc()
        