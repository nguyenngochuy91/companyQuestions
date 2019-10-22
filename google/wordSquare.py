# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:28:16 2019

@author: huyn
"""

#Word Squares
#Given a set of words (without duplicates), find all word squares you can build from them.
#
#A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
#For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
from typing import List
def wordSquares(words: List[str]) -> List[List[str]]:
    
    return