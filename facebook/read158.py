# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:22:43 2019

@author: huyn
"""

#158. Read N Characters Given Read4 II - Call multiple times
#Given a file and assume that you can only read the file using a given method read4, 
#implement a method read to read n characters. Your method read may be called multiple times.
#
# 
#
#Method read4:
#
#The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
#
#The return value is the number of actual characters read.
#
#Note that read4() has its own file pointer, much like FILE *fp in C.
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.string = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        check = False
        for i in range(min(n,len(self.string))):
            buf[i]=self.string[i]
            n-=1
            check = True
        if check:
            i+=1
        else:
            i =0
        self.string = self.string[i:]
        while n>0:
            b = [""]*4
            size = read4(b)
            if size ==0:
                return i
            else:
                for index in range(min(size,n)):
                    buf[i] = b[index]
                    i+=1
                    n-=1
                for j in range(index+1,size):
                    self.string.append(b[j])
        return i