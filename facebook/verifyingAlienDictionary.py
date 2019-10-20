# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 03:04:33 2019

@author: huyn
"""
from typing import List
#Verifying an Alien Dictionary
#In an alien language, surprisingly they also use english lowercase letters, but 
#possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
#Given a sequence of words written in the alien language, and the order of the alphabet, 
#return true if and only if the given words are sorted lexicographicaly in this alien language.
def isAlienSorted(words: List[str], order: str) -> bool:
    d = {}
    
    for i in range(26):
        d[order[i]]=i
    for i in range(len(words)-1):
        w1 = convert(d,words[i])
        w2 = convert(d,words[i+1])
       
        check = None
        for i in range(min(len(w1),len(w2))):
            if w1[i]>w2[i]:
                check = False
                break
            elif w1[i]==w2[i]:
                continue
            else:
                check = True
                break
        if check == False:
            return False
        if check == None:
            if len(w1)>len(w2):
                return False
        
                
    return True
def convert(d,word):
    w = []
    for l in word:
        w.append(d