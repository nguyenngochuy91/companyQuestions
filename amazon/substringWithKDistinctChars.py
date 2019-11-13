# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:40:25 2019

@author: huyn
"""
"""
Substrings with exactly K distinct chars
Given a string s and an int k, return an int representing the number of substrings 
(not unique) of s with exactly k distinct characters. If the given string doesn't 
have k distinct characters, return 0.

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]

Input: s = "aabab", k = 3
Output: 0
"""
def countSubstring(s,k):
    d= {0:1}
    count = 0
    letters = set()
    for letter in s:
        letters.add(letter)
        size = len(letters)
        if size not in d:
            d[size] = 0
        d[size] += 1
        if size- k in d:
            count += d[size-k]
    print (d)
    return count

s = "pqpqs"
k = 2
print (countSubstring(s,k))

def countMax(s,k):
    