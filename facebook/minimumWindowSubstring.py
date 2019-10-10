# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:57:26 2019

@author: Huy Nguyen
"""

#Minimum Window Substring
#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
def minWindow(str1: str, str2: str) -> str:
    if str2 in str1:
        return str2

    d = {}
    for l in str2:
        if l not in d:
            d[l]=0
        d[l]+=1
    # number of different character, use this to mark if we already match str2
    hitting = 0
    start,stop = 0,0
    currentD = {}
    output = ""
    while stop<len(str1):
        letter = str1[stop]
        if letter not in currentD:
            currentD[letter]=0
        currentD[letter]+=1
        if letter in d and d[letter]==currentD[letter]:
            hitting+=1
#        print (currentD,hitting)
        # if we hit the form, we will retract just like our template, we retract as long as our hitting is still equal to len(d)
        while hitting ==len(d) and start<stop:
#            print ("inner loop")
            # we check if our current is the smallest string
            if not output:
                output = str1[start:stop+1]
#                print (84,output)
            else:
                if (stop-start+1)<len(output):
                    output = str1[start:stop+1]
#                    print (88,output)

            # get the character on start
            leftMostLetter =str1[start]
#            print ("leftMostLetter",leftMostLetter)
            # decrease our count
            currentD[leftMostLetter]-=1
#            print (currentD)
            if leftMostLetter in d and currentD[leftMostLetter]<d[leftMostLetter]:
                hitting-=1

            # increment our start
            start+=1
        # increment our stop
        stop+=1  

    return output