# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:50:41 2019

@author: huyn
"""

#Decode String
#Given an encoded string, return its decoded string.
#
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being 
#repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
#You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
#Furthermore, you may assume that the original data does not contain any digits and that digits are only for those 
#repeat numbers, k. For example, there won't be input like 3a or 2[4].

def decodeString(s: str) -> str:
    res = ""
    stack = []
    for item in s:
        # if it is alpha, we just add to our res
        if item.isalpha():
            if not stack:
                res+=item
            else:
                stack.append(item) 
        elif item.isdigit():
            if not stack:
                stack.append(item)
            else:
                if stack[-1].isdigit(): # case 23[ab]
                    stack[-1]+=item
                else:
                    stack.append(item) # case ab3[2[a]b]
        elif item == "[": # we start adding either number or char after
            stack.append("[")
        else: # case "]"
            # we need to pop
            string = ""
            while stack[-1].isalpha(): # we stop when hitting "["
                string += stack.pop()[::-1]
            # we pop the "["
            stack.pop()
            # we get the number
            number = int(stack.pop())
            if stack:
                stack.append(string[::-1]*number)
            else:
                res += string[::-1]*number
#        print (item,stack,res)
    return res
#s = "3[a]2[bc]"
#print (decodeString(s))
#s = "3[a2[c]2[m3[fc]]]"
#print (decodeString(s))
s = "1[1[jk]e1[f]]"
print (decodeString(s))