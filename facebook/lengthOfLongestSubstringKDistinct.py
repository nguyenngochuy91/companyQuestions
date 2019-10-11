# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:39:41 2019

@author: huyn
"""

#340. Longest Substring with At Most K Distinct Characters
#Given a string, find the length of the longest substring T that contains at most k distinct characters.
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    start,stop = 0,0
    dictionary = {} # this will keep track of how many distinct characters we have and how many of it we have in the current window
    length = 0 # keep track of how long was our substring
    maxLength = 0 # our output
    while stop<len(s):
        currentLetter = s[stop]
        if currentLetter in dictionary:
            dictionary[currentLetter]+=1
            length+=1
        else:
            # 2 cases, if our len(dic) already hit k, this will increase our number of distinct, we need to decrease our unique key before adding this
            # we also need to record our length as max if it is greater than maxlength
            maxLength =max(length,maxLength)
            while len(dictionary)==k: # we dont need to add the start<stop since we know k>=1, we will never have to increase start = stop
                lastLetter = s[start]
                # decrement the count by 1
                dictionary[lastLetter]-=1
                length-=1
                # pop out the last letter if hits 0
                if dictionary[lastLetter]==0:
                    dictionary.pop(lastLetter)
                    # it will break the loop after this
                start+=1
            # now we can add our currentLetter
            if currentLetter not in dictionary:
                dictionary[currentLetter]=0
            dictionary[currentLetter]+=1 # increment our count
            length+=1 # increment our length
        stop+=1
    return max(length,maxLength) # might be a case we dont hit the amount of key, but still greater than maxLength