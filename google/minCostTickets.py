#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:19:28 2020

@author: huynguyen
"""


# 983. Minimum Cost For Tickets
# In a country popular for train travel, you have planned some train travelling one year in advance.
#   The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

# Train tickets are sold in 3 different ways:

# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2,
#  then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

# Return the minimum number of dollars you need to travel every day in the given list of days.
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = {}
        def dfs(day):
            if day>365:
                return 0
            elif day not in days:
                return dfs(day+1)
            else:
                if day in d:
                    return d[day]
                else:
                    v = min([dfs(day+1)+costs[0],dfs(day+7)+costs[1],dfs(day+30)+costs[2]])
                    d[day] = v
                    return v
        return dfs(1)
            