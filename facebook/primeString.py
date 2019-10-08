# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:59:47 2019

@author: huyn
"""

# Prime String
# Given a string consisting of English letters both lowercase and uppercase. 
# Your task is to convert it to the prime word. Prime word is a word consisting 
# of only prime characters and prime character is a letter whose ASCII code is prime. 
# Each non-prime character is equidistant with 2 prime characters the one with lower 
# ASCII value will be consider as its replacement.
#
#Constraints
#1 <= string length <= 5000
#
#Example
#Input: ABc
#Output: CCa
def isPrime(val):
    for i in range(2,int(val**.5)):
        if val%i==0:
            return False
    return True
def getPrimeString(string):
    letter="qwertyuiopasdfghjklzxcvbnm"
    upperLetter = letter.upper()
    letter +=upperLetter
    letter = sorted(letter)
    d = {}
    v = {}
    res = ""
    notAssigned = []
    for l in letter:
        val = ord(l)
        if isPrime(val):
            d[l] = l
            v[val]=l
        else:
            notAssigned.append(l)
    
    choices = sorted(v)
    for letter in notAssigned:
        val =ord(letter)
        start,stop =0,len(choices)-1
        while start+1<stop:
            mid = (start+stop)//2
            if choices[mid]>val:
                stop=mid
            else:
                start=mid
        if choices[start]>val:
            d[letter] = v[choices[start]]
        elif choices[stop]<val:
            d[letter] = v[choices[stop]]
        elif val- choices[start]<=choices[stop]-val:
            d[letter] = v[choices[start]]
        else:
            d[letter] = v[choices[stop]]
#    print (d)
    for s in string:
        res+=d[s]
    return res
a= "ABc"
#print (getPrimeString(a))
