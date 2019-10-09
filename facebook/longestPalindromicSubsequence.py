# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:01:29 2019

@author: huyn
"""
#516. Longest Palindromic Subsequence
#Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

s="bbbab"
s="cbbd"
# version used palindrome Substring
def longestPalindromeSubseq(s: str) -> int:
    arr =[]
    n = len(s)
    maxLength = 0
    for i in range(n):
        t= []
        for j in range(n):
            if i==j:
                t.append(1)
                maxLength = 1
            else:
                t.append(0)
        arr.append(t)
    for i in range(1,n):
        for j in range(1,n):
            if i!=j:
                if s[i]==s[j]:
                    arr[i][j] = arr[i-1][j-1]+2
                else:
                    arr[i][j] = max(arr[i-1][j],arr[i][j-1])
                maxLength = max(maxLength,arr[i][j])
    return maxLength

