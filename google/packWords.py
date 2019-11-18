# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:26:14 2019

@author: huyn
"""
"""
Pack words
n by n matrix of random letter, and a dictionary of words. Find the maximum number 
of words that can be packed on the board from the given dictionary
A word is considered to be able to be packed on the board if 
    it can be found in the dictionary
         It can be constructed from untaken letters by other words found so far
         in the board
             the leters are adjacent to each other
             
Each tile can be visited only once by any word
["eat","rain","in","rat"]
[["e","a","n"],
["t","t","i"],
["a","r","a"]]
return 3 
"""
def findMaximumWords(words,matrix):
    return