# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:07:11 2019

@author: Huy Nguyen
"""

#Read N Characters Given Read4
def read4(buf):
    return
def read(buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """
    smallBuf = [""]*4 # where we store the read4
    i = 0
    while n>0:
        inputRead = read4(smallBuf)
        for j in range(min(n,inputRead)):
            buf[i]=smallBuf[j]
            n-=1
            i+=1
        # we are done if either n==0 (which is check by the while loop condition) or inputRead less than 4 and we use all of them
        if inputRead<4:
            break
    return i