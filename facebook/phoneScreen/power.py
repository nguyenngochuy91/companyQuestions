# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 02:13:16 2019

@author: huyn
"""

# power to 
def myPow(x,n):
    if n==0:
        return 1
    if x== 0:
        return 0
    if x==1 or x==-1:
        if n%2==0:
            return 1
        else:
            return -1
    if x<0:
        return -myPow(x,n)
    if n <0:
        return 1/(myPow(x,-n))
    if n%2==0:
        return myPow(x,n//2)*myPow(x,n//2)
    else:
        return myPow(x,n//2)*myPow(x,n//2)*x