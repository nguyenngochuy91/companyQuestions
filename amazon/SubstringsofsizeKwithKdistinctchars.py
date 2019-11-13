# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:34:15 2019

@author: huyn
"""
"""
Substrings of size K with K distinct chars
Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
"""
def substringOfSizeKWithKDistinctChars(s,k):
    res = {}
    d = {}
    count  = 0
    for i in range(k):
        letter = s[i]
        if letter not in d:
            d[letter] = 0
        d[letter]+=1
    if len(d) == k:
        res[s[:k]] = count
        count += 1
    for i in range(k,len(s)):
        newLetter = s[i]
        firstLetter = s[i-k]
        # remove firstLetter
        d[firstLetter] -= 1
        if d[firstLetter] == 0:
            d.pop(firstLetter)
        if newLetter not in d:
            d[newLetter] = 0
        d[newLetter] += 1
        string = s[i-k+1:i+1]
        if len(d) == k and string not in res:
            res[string] = count
            count += 1
    return sorted(res,key = lambda x: res[x] )

s = "abcabc"
k = 3
print (substringOfSizeKWithKDistinctChars(s,k))  
s = "abacab"
k = 3
print (substringOfSizeKWithKDistinctChars(s,k))  
s = "awaglknagawunagwkwagl"
k = 4
print (substringOfSizeKWithKDistinctChars(s,k))  