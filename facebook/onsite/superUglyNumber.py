# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:16:19 2019

@author: huyn
"""

#313. Super Ugly Number
#Write a program to find the nth super ugly number.
#
#Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        answer = []
        found  = set()
        current = [1]
        while len(answer) < n:
            minimum = heapq.heappop(current)
            if minimum not in found:
                found.add(minimum)
                answer.append(minimum)
                for p in primes:
                    heapq.heappush(current,minimum*p)
        return answer[n-1]
            
        
n = 12
primes = [2,7,13,19]