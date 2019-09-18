# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:43:00 2019

@author: huyn
"""

#91. Decode Ways
#A message containing letters from A-Z is being encoded to numbers using the following mapping:
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number of ways to decode it
def numDecodings(s: str) -> int:
    if not s:
        return 0
    if s[0]=="0":
        return 0
    if len(s)==1:
        return 1
    arr= [0,0]
    if check(s[-1]):
        arr[0]+=1
    if check(s[-2]) and arr[0]:
        arr[1]+=1
    if check(s[-2]+s[-1]):
        arr[1]+=1
    print (arr)
    for i in range(len(s)-3,-1,-1):
        val =0
        if check(s[i]+s[i+1]) and arr[0]:
            val+=arr[0]
        if check(s[i]) and arr[1]:
            val+=arr[1]
        arr[0],arr[1]=arr[1],val

    return arr[1]
# check function to verify a valid step
def check(string):
#    print (string)
    if int(string)>26 or int(string)==0:
        return False
    if "0" in string:
        return string in ["10","20"]
    return True

#string = "12312731"
#print (numDecodings(string))
#string = "1232312321212"
#print (numDecodings(string))