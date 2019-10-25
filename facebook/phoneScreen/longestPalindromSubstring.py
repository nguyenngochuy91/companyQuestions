# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:51:56 2019

@author: huyn
"""
# O(n**2)
def longestPalindrome(s):
    if not s:
        return ""
    length = 1
    output = s[0]
    for i in range(len(s)):
        j,k =i,i
        while j>=0 and k<len(s):
            if s[j]!=s[k]:
                break
            j-=1
            k+=1
       
        if k-j-1>length:
            output=s[j+1:k]
        length= max(length,k-j-1)            
        j,k= i, i+1
        while j>=0 and k<len(s):
            if s[j]!=s[k]:
                break  
            j-=1
            k+=1
        if k-j-1>length:
            output=s[j+1:k]
        length= max(length,k-j-1)
    return output

#s = "babad"
#print (longestPalindrome(s))
#s = "bb"
#print (longestPalindrome(s))
# O(n)
def longesPalindromeBest(s):
    return