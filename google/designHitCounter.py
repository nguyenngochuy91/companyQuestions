# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:25:07 2019

@author: huyn
"""

#362. Design Hit Counter
#Design a hit counter which counts the number of hits received in the past 5 minutes.
#
#Each function accepts a timestamp parameter (in seconds granularity) and you may assume
# that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing).
# You may assume that the earliest timestamp starts at 1.
#
#It is possible that several hits arrive roughly at the same time.

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.d   = {}
        self.size = 0
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.size +=1
        if timestamp not in self.d:        
            self.arr.append(timestamp)
            self.d[timestamp] = self.size
        else:
            # if already in, we just update our timestamp count
            self.d[timestamp] += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.arr:
            return 0
        start = 0
        stop = len(self.arr)-1
        while start + 1 <stop:
            mid = (start+stop)//2
            val = self.arr[mid]
            if val>timestamp-300:
                stop = mid
            else:
                start = mid

        if self.arr[start]>timestamp-300:
            # check if start is actually at 0
            if start == 0:
                return self.size
            else:
                item = self.arr[start-1]
                return self.size - self.d[item]
        elif self.arr[stop]>timestamp-300:
            item = self.arr[stop-1]
            return self.size  - self.d[item]
        return 0



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)