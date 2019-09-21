# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:39:41 2019

@author: huyn
"""

#340. Longest Substring with At Most K Distinct Characters
#Given a string, find the length of the longest substring T that contains at most k distinct characters.
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    output = 0
    d= {}
    start,stop = 0,0
    length = 0
    while stop<len(s):
        letter = s[stop]
        print (d,start,stop)
        if letter not in d:
            if len(d)<k:
                d[letter]=1
                length+=1
            else:
                # we have to remove some letter until we can put this in
                output = max(length,output)
                while len(d)>=k:
                    lastLetter = s[start]
                    d[lastLetter]-=1
                    start+=1
                    length-=1
                    if d[lastLetter]==0:
                        d.pop(lastLetter)
                        break
                d[letter]=1
        else:
            length+=1
            d[letter]+=1
        stop+=1
    return max(output,length)
s ="qtttqywywyiwiwieioqppppqqq"
k = 3
print (lengthOfLongestSubstringKDistinct(s,k))