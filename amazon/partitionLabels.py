# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:56:28 2019

@author: huyn
"""
"""
763. Partition Labels
A string S of lowercase letters is given. We want to partition this string into
 as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        globalSet = set()
        array = [] # array that store set of letter 
        res = [] # array that store what index do we have a new splitting part
        for i in range(len(S)):
            letter = S[i]
            if letter not in globalSet: # we can start a new set letter right here
                # we add this letter to our globalSet
                globalSet.add(letter)
                # create a set letter to add to array
                array.append(set(letter))
                # we append this index to res as a starting of a new part 
                res.append(i)
            else:
                # we pop our array and res until we hit a set that contain this letter 
                # we also need to accumulate the set of letter we thought to make a new part to add to previous
                # example : aaaaaabcd a, then we have to add bcd to set a
                accumulate = set()
                while letter not in array[-1]:
                    accumulate.update(array.pop())
                    res.pop()
                array[-1].update(accumulate)
        # we append the len S to the end of res
        res.append(len(S))
        # now we iterate through our array and report the result
        output = []
        for i in range(1,len(res)):
            output.append(res[i]-res[i-1])
        return output