# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:28:17 2019

@author: Huy Nguyen
"""

#Implement Buffer with the following api
#class Buffer {
#	
#	public Buffer(int capacity) {
#	}
#
#	/**
#	* Transfers the content of the given source char array into this buffer.
#	* Returns the the number of chars that were written into the buffer.
#	*/
#	public int write(char[] src) {
#	}
#
#	public char[] read(int n) {
#	}
#}
from collections import deque
class Buffer:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data     = deque([])
    def write(self,string):
        count =0 
        for i in range(min(len(string),self.capacity-len(self.data))):
            self.data.append(string[i])
            count+=1
        return count
    def read(self,n):
        string = ""
        for i in range(min(n,len(self.data))):
            string+=self.data.popleft()
        return string
        
myBuffer = Buffer(5)
print (myBuffer.write("abc"))

print (myBuffer.write("def"))
print (myBuffer.read(3))

print (myBuffer.write("xyzabc"))

print (myBuffer.read(8))

