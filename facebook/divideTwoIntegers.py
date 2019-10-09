# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:31:03 2019

@author: huyn
"""

#29. Divide Two Integers
#Given two integers dividend and divisor, divide two integers without using multiplication, 
#division and mod operator.
#
#Return the quotient after dividing dividend by divisor.
#
#The integer division should truncate toward zero.
def divideNaive(dividend,divisor):
    c = 0
    if dividend==0:
        return 0
    if divisor == 1:
        return dividend
    if divisor ==-1:
        return -dividend
    a,b = abs(dividend),abs(divisor)
    while a>=b:
        c+=1
        a-=b
    if dividend>0 and divisor>0 or dividend<0 and divisor<0:
        return c
    else:
        return -c
#print (divideNaive(5,3))
#print (divideNaive(10,3))
#print (divideNaive(5,2))
#print (divideNaive(-12,3))
#print (divideNaive(-12,1))

def divideBinary(dividend,divisor):
    if dividend<0:
        return -divideBinary(-dividend,divisor)
    if divisor <0:
        return -divideBinary(dividend,-divisor)
    if divisor>dividend:
        return 0
    if dividend ==0:
        return 0
    if divisor ==1:
        return dividend
    
        
            
    