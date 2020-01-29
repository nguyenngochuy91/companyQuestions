# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:43:07 2020

@author: huyn
"""

#252. Meeting Rooms
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            first = intervals[i]
            second = intervals[i+1]
            if max(first)> min(second):
                return False
        return True