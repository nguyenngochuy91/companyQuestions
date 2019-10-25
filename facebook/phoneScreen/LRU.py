# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:29:17 2019

@author: huyn
"""
#rderedDict is a subclass of dict, and needs more memory to keep track of the order
# in which keys are added. This isn't trivial. The implementation adds a second dict 
# under the covers, and a doubly-linked list of all the keys (that's the part that remembers the order), 
# and a bunch of weakref proxies. It's not a lot slower, but at least doubles the memory over using a 
# plain dict.
#
#But if it's appropriate, use it! That's why it's there :-)
# But if this were a Python list, deleting a key would take O(n) time twice over: 
#O(n) time to find the key in the list, and O(n) time to remove the key from the list.

#So it's a doubly-linked list instea
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key) # we use this, so we make it most recent again
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False) # pop the least used, which is order the first