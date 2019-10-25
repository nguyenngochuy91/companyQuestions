# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:46:53 2019

@author: huyn
"""

#Anagram Substring Search (Or Search for all permutations)
#Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) 
#that prints all occurrences of pat[] and its permutations (or anagrams) in txt[]. You may assume that n > m.
#Expected time complexity is O(n)
def findAllAnagram(txt,pattern):
    res = []
    d = {}
    currentD   = {}
    for letter in pattern:
        if letter not in d:
            d[letter]=0
        if letter not in currentD:
            currentD[letter] = 0
        d[letter]+=1
    start,stop = 0,0
    length     = 0
    print (currentD,d)
    while stop<len(txt):
        print (start,stop,res,currentD)
        currentLetter = txt[stop]
        if currentLetter not in d:
            for i in range(start,stop):
                currentD[txt[i]]-=1
            start,stop = stop+1,stop+1
            length = 0
        else:
            print ("currentLetter",currentLetter)
            if currentD[currentLetter]<d[currentLetter]:
                currentD[currentLetter]+=1
                length +=1
                if length == len(pattern):
                    res.append(start)
                stop+=1
            else:
                # we currently have currentD[currentLetter] == d[currentLetter]
                # we have to move start until we hit the same current letter, or we can't move tstop at all
                while start<stop and currentD[currentLetter] == d[currentLetter]:
                    lastLetter = txt[start]
                    currentD[lastLetter]-=1
                    length-=1
                    start+=1
                # eventually, we will have currentD[currentLetter]<d[currentLetter]
                currentD[currentLetter]+=1
                length+=1
                stop+=1
                if length == len(pattern):
                    res.append(start)
    return res
txt= "AAABABAA"
pattern ="AABA"
print (findAllAnagram(txt,pattern))