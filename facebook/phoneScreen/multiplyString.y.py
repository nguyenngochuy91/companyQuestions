# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:08:47 2019

@author: Huy Nguyen
"""

#Multiply Strings   
#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
def multiply(self, num1: str, num2: str) -> str:
    if len(num2)>len(num1):
        num1,num2=num2,num1
    num1 = [int(item) for item in num1]
    num2 = [int(item) for item in num2]
    listToAdd= []
    for i in range(len(num2)-1,-1,-1):
        over= 0
        string = [0]*(len(num2)-i-1)
        n1 = num2[i]
        if n1==0:
            continue
        for j in range(len(num1)-1,-1,-1):
            val = num2[i]*num1[j]+over
            string.append(val%10)
            over = val//10
        if over:
            string.append(over)
        listToAdd.append(string)
    return addAll(listToAdd)
        
def addAll(listToAdd):
    if len(listToAdd)==0:
        return "0"
    elif len(listToAdd)==1:
        return "".join([str(item) for item in listToAdd[0][::-1]])
    else:
        first = add2List(listToAdd[0],listToAdd[1])
        for eachList in listToAdd[2:]:
            second = add2List(first,eachList)
            first  = second
        return "".join([str(item) for item in first[::-1]])
def add2List(list1,list2):
    res =[]
    over = 0
    for i in range(min(len(list1),len(list2))):
        n1 = list1[i]
        n2 = list2[i]
        val = n1+n2+over
        res.append(val%10)
        over = val//10
    for item in list1[i+1:]:
        val = item+over
        res.append(val%10)
        over = val//10      
    for item in list2[i+1:]:
        val = item+over
        res.append(val%10)
        over = val//10
    if over:
        res.append(over)
    return res