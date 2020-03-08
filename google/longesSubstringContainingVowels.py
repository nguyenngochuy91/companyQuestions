# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:57:55 2020

@author: huyn
"""

#1371. Find the Longest Substring Containing Vowels in Even Counts
#Given the string s, return the size of the longest substring containing each vowel 
#an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        d = {"00000":-1}
        maxLength = 0
        vowels = {letter:0 for letter in "aeiou"}
        for index,letter in enumerate(s):
            if letter in "aeiou":
                vowels[letter] = (vowels[letter]+1)%2
            string = ""
            for letter in "aeiou":
                string += str(vowels[letter])
            if string not in d:
                d[string] = index
            else:
                lastIndex = d[string]
                maxLength = max(maxLength,index-lastIndex)
        return maxLength