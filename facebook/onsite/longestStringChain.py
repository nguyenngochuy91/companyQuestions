# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:10:14 2019

@author: Huy Nguyen
"""
"""
Longest String Chain
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 
to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, 
word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words."""
from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = {} # map a word to potential ancestor : ab -> [*ab,a*b,ab*]
        v = {} # map a potential *ab to potential predecessor: 3:{*ab: [aab,bab,wab,...],a*b:[aab,axb,...]}
        for word in words:
            size = len(word)
            d[word] = []
            if size not in v:
                v[size] = {}
            for i in range(size+1):
                ancestor = word[:i]+"*"+word[i:]
                d[word].append(ancestor)
                if i!=size:
                    string = word[:i]+"*"+word[i+1:]
                    if string not in v[size]:
                        v[size][string] = []
                    v[size][string].append(word)
                    
        dp = {}
        self.res = 1
        def dfs(currentWord):
#            print (currentWord)
            dp[currentWord] = 1
            for possibleAncestor in d[currentWord]:
                if len(possibleAncestor) in v:
                    if possibleAncestor in v[len(possibleAncestor)]:
                        for nextWord in v[len(possibleAncestor)][possibleAncestor]:
                            if nextWord not in dp:
                                dp[nextWord] = dfs(nextWord)
                            dp[currentWord] = max(dp[currentWord],1+dp[nextWord])
                else: # means that there are no next step
                    return dp[currentWord]
            self.res = max(dp[currentWord],self.res)
            return dp[currentWord]

        for word in words:
            if word not in dp:
                dfs(word)
#        print (dp)
        return self.res
                