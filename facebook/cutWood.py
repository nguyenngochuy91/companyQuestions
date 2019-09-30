# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:11:29 2019

@author: Huy Nguyen
"""

#Cut Wood
#Given an int array wood representing the length of n pieces of wood and an int k.
# It is required to cut these pieces of wood such that more or equal to k pieces of the same
# length len are cut. What is the longest len you can get?
def cutWood(woods,k):
    start = 1
    stop  = max(woods)
    while start+1<stop:
        mid = (start+stop)//2
        val = check(woods,mid)
        if val>=k:
            start = mid
        else:
            stop = mid
    if check(woods,stop)>=k:
        return stop
    if check(woods,start)>=k:
        return start
    return 0
def check(woods,num):
    c =0
    for wood in woods:
        c+=wood//num
    return c

#woods =[ 5, 9, 7]
#k= 3
#print (cutWood(woods,k))
#wood = [5, 9, 7]
#k = 4
#print (cutWood(woods,k))
woods= [1, 2, 3]
k=7
print (cutWood(woods,k))
#woods= [232, 124, 456]
#k = 7
#print (cutWood(woods,k))