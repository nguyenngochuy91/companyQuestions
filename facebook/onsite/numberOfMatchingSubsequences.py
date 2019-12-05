# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 07:53:53 2019

@author: Huy Nguyen
"""
"""
792. Number of Matching Subsequences
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace"."""
from typing import List
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        wordDict = {letter:[] for letter in "qwertyuiopasdfghjklzxcvbnm"}
        for word in words:
            iterator = iter(word)
            letter = next(iterator)
            wordDict[letter].append(iterator)
        for letter in S:
            currentWordStartWithLetter = wordDict[letter]
            wordDict[letter] = []
            # reset this to empty list
            for iterator in currentWordStartWithLetter:
                nextLetter = next(iterator,None)
                if nextLetter:
                    wordDict[nextLetter].append(iterator)
                else:
                    count+=1
        return count