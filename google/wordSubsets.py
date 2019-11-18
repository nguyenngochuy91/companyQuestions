# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 01:39:02 2019

@author: huyn
"""
"""
916. Word Subsets
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity. 
 For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

"""
from typing import List
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        myList = [0]*26
        for string in B:
            smallList = [0]*26
            for letter in string:
                smallList[ord(letter)-97]+=1
            for i in range(26):
                myList[i] = max(myList[i],smallList[i])
        res = []

        for string in A:
            smallList = [0]*26
            for letter in string:
                smallList[ord(letter)-97]+=1
            check = True
            for i in range(26):
                if smallList[i]<myList[i]:
                    print (string,i)
                    check = False
                    break
            
            if check:
                res.append(string)
        return res