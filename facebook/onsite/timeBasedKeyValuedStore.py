# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 03:04:16 2019

@author: huyn
"""
"""
981. Time Based Key-Value Store
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
"""
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([timestamp,value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.d:
            return ""
        myList = self.d[key]

        start, stop = 0, len(myList)-1
        while start+1 <stop:
            mid = (start+stop)//2
            time,val = myList[mid]
            if time>timestamp:
                stop = mid
            else:
                start = mid
        if myList[stop][0]<=timestamp:
            return myList[stop][1]
        if myList[start][0] <= timestamp:
            return myList[start][1]
        return ""
        


#Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
#Output: [null,null,"bar","bar",null,"bar2","bar2"]
#Explanation:   
#TimeMap kv;   
#kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
#kv.get("foo", 1);  // output "bar"   
#kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
#kv.set("foo", "bar2", 4);   
#kv.get("foo", 4); // output "bar2"   
#kv.get("foo", 5); //output "bar2"

#Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], 
#inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
#Output: [null,null,null,"","high","high","low","low"]