# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:12:06 2019

@author: huyn
"""

#Best Time To Buy And Sell Stock III
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock
before you buy again)."""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        
            
arr = [3,3,5,0,0,3,1,4]
