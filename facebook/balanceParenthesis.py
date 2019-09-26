# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:44:18 2019

@author: huyn
"""

#Balance the parenthesis in a string
#You are given a string with alphanumeric characters and parentheses. Your goal 
#is to return a string with balanced parentheses by removing the fewest characters possible. 
#Note that you cannot add anything to the string.
#"()"  -> "()"
#"b(a)r)"  -> "b(a)r"
#")("  -> ""
#"((((("  -> ""
#")(())("  -> "(())"
#string = ")(())("
def balance_parens_naive(string):
    stack = []
    indices = []
    for index,item in enumerate(string):
        if item ==")":
            if not stack:
                indices.append(index)
            else:
                stack.pop()
        elif item =="(":
            stack.append(index)
    indices.extend(stack)
    return "".join([string[i] for i in range(len(string)) if i not in indices])
# O(n) time, O(n) space
def balance_parens_1(string):
    string = list(string)
    stack = []
    for index,item in enumerate(string):
        if item ==")":
            if not stack:
                string[index]=""
            else:
                stack.pop()
        elif item =="(":
            stack.append(index)
    for index in stack:
        string[index] = ""
    return "".join(string)
#print (balance_parens_naive(string))
#print (balance_parens_1(string))

#Approach 5: Keep a counter to track parens, 3 passes, mutate original string (O(n) time and O(1) space)
def balance_parens_2(string):
    countL = 0
    string = list(string)
    for index,item in enumerate(string):
        if item ==")":
            if not countL:
                string[index]=""
            else:
                countL-=1
        elif item =="(":
            countL+=1
    countR = 0
#    print (string)
    for index in range(len(string)-1,-1,-1):
        item = string[index]
        if item =="(":
            if not countR:
#                print (index)
                string[index]=""
            else:
                countR-=1
        elif item ==")":
            countR+=1
    return "".join(string)
string = ")(())("    
print (balance_parens_2(string))