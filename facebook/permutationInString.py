# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 01:45:51 2019

@author: huyn
"""

#Permutation in String
#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
#In other words, one of the first string's permutations is the substring of the second string.
def checkInclusion(s1: str, s2: str) -> bool:
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    d1 = {alphabet[i]:0 for i in range(26)}
    words = set()
    for l in s1:
        d1[l]+=1
        words.add(l)
    d2 = {alphabet[i]:0 for i in range(26)}
    start , stop = 0,0
    length  = 0
    while stop <len(s2):
        currentLetter = s2[stop]
        stop+=1
        if d1[currentLetter]:
            d2[currentLetter]+=1
#            print (d1[currentLetter],d2[currentLetter])
            if d2[currentLetter] == d1[currentLetter]:
                length+=1
                if length == len(words):
                    if stop-start ==len(s1):
                        return True
                # means that we cover all the letter, now we contract our start,stop so that the stop-start == len(s2)
                    while (stop-start)>len(s1) and start<stop:
                        firstLetter = s2[start]
                        d2[firstLetter]-=1
                        if d2[firstLetter]<d1[firstLetter]:
                            length-=1
                            break
                        start+=1
                    if length == len(words) and stop-start==len(s1):
                        return True
                    
        else:
            start = stop
            d2 = {alphabet[i]:0 for i in range(26)}
            length = 0
#        print (start,stop,length, d2,words,length)
    return length == len(words) and stop-start==len(s1)
s1,s2="a","aa"
print(checkInclusion(s1,s2))
