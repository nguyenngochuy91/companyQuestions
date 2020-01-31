# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:59:07 2020

@author: huyn
"""

#475. Heaters
from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius = 0
        currentHeater = None
        heaters = set([heater-1 for heater in heaters])
        for index,house in enumerate(houses):
            if index in heaters:
                if currentHeater == None:
                    radius = max(radius,index-0)
                else:
                    radius = max(radius,(index-currentHeater)//2)
                currentHeater = index
        radius = max(radius,len(houses)-1-currentHeater)
        return radius