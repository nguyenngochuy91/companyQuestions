# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:07:54 2019

@author: huyn
"""
from collections import deque
#Palindromic Subsequences
#Given a string s, return all palindromic subsequences of s.
def findPalindromicSubsequencesNaive(s):
    res=deque([""])
    for letter in s:
        size = len(res)
        for i in range(size):
            item = res.popleft()
            res.append(item+letter)
            res.append(item)
    return [item for item in res if checkPalindrome(item)]
def checkPalindrome(string):
    if not string:
        return False
    for i in range(len(string)//2):
        if string[i]!=string[len(string)-1-i]:
            return False
    return True
#s = "abac"
#print (findPalindromicSubsequencesNaive(s))
def findPalindromeDP(s):
    res = []
    return res
    
s='abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'