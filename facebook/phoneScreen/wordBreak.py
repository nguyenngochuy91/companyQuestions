# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:11:50 2019

@author: huyn
"""
from typing import List
#Word Break
#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
#determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
#Note:
#
#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
def wordBreak(s: str, wordDict: List[str]) -> bool:
    if s in wordDict:
        return True
    d= {}
    def dfs(start,stop):
        if start == stop:
            return True
        elif start<stop:
            for i in range(start+1,stop):
                string1= s[start:i]
                string2 = s[i:stop]
                if string1 not in d:
                    d[string1] = dfs(start,i) or string1 in wordDict

                if string2 not in d:
                    d[string2] = dfs(i,stop) or string2 in wordDict
                if d[string1] and d[string2]:

                    return True
            return False
#    print (d)
    return dfs(0,len(s))
s = "leetcode"
wordDict = ["leet", "code"]
print (wordBreak(s,wordDict))
s = "applepenapple"
wordDict = ["apple", "pen"]
print (wordBreak(s,wordDict))
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print (wordBreak(s,wordDict))