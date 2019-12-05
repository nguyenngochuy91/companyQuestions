# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 02:41:35 2019

@author: Huy Nguyen
"""
"""
1054. Distant Barcodes
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists"""
import heapq
from typing import List
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = {}
        for item in barcodes:
            if item not in d:
                d[item] = 0
            d[item]+=1
        queue = []
        for key in d:
            heapq.heappush(queue,[-d[key],key])
        res = []
        while queue:
            val1, item1 = heapq.heappop(queue)
            if res:
                if res[-1] == item1:
                    val2, item2 = heapq.heappop(queue)
                    res.append(item2)
                    if val2+1!=0:
                        heapq.heappush(queue,[val2+1,item2])
                    heapq.heappush(queue,[val1, item1])
                    continue
            res.append(item1)
            if val1+1!=0:
                heapq.heappush(queue,[val1+1, item1])
        return res