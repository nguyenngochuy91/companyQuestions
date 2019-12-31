#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:10:25 2019

@author: huyn
"""

#256. Paint House
#There are a row of n houses, each house can be painted with one of the three colors: 
#    red, blue or green. The cost of painting each house with a certain color is different. 
#    You have to paint all the houses such that no two adjacent houses have the same color.
#
#The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
#For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost
# of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
#
#Note:
#All costs are positive integers.

from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        array = costs[0]
        for i in range(1,len(costs)):
            nextRow = costs[i]
            temp = [0,0,0]
            temp[0]  = min(array[1],array[2]) + nextRow[0]
            temp[1]  = min(array[0],array[2]) + nextRow[1]
            temp[2]  = min(array[1],array[0]) + nextRow[2]
            array = temp
        return min(array)