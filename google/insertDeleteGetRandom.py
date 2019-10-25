# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:24:12 2019

@author: huyn
"""
#Insert Delete GetRandom O(1)
#Design a data structure that supports all following operations in average O(1) time.
#
#insert(val): Inserts an item val to the set if not already present.
#remove(val): Removes an item val from the set if present.
#getRandom: Returns a random element from current set of elements. 
#Each element must have the same probability of being returned.
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.d[val]=1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            self.d.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(list(self.d.keys()))
