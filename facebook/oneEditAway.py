# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:31:26 2019

@author: huyn
"""
#Write a function to return if two words are exactly "one edit" away, where an edit is:
#Inserting one character anywhere in the word (including at the beginning and end)
#Removing one character
#Replacing exactly one character
def isOneEditAway(w1,w2):
    if abs(len(w1)-len(w2))>=2:
        return False
    if len(w1)==len(w2):
        count = 0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                if count ==1:
                    return False
                elif count==0:
                    count+=1
        return count==1
    else:
        i,j=0,0
        while i<len(w1) and j<len(w2):
            char1= w1[i]
            char2= w2[j]
            if char1==char2:
                i+=1
                j+=1
            else:
                return w1[i+1:]==w2[j:] or w2[j+1:]==w1[i:]
        return True
print (isOneEditAway("abcmef","abcef"))
print (isOneEditAway("cat", "dog"))
print (isOneEditAway("cat", "cats"))
print (isOneEditAway("cat", "cut"))
print (isOneEditAway("cat", "cast"))
print (isOneEditAway("cat", "at"))
print (isOneEditAway("cat", "act"))