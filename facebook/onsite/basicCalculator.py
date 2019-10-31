# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 02:47:41 2019

@author: huyn
"""
"""
224. Basic Calculator
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or 
minus sign -, non-negative integers and empty spaces ."""
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            else:
                if num:
                    val = int(num)
                    stack.append(val)
                    num = ""
                # check char if is an operation
                if char in "+-(":
                    stack.append(char)
                elif char == ")":
                    # we start popping until we hit (
                    acc = 0
                    while True:
                        val = stack.pop()
                        op = None
                        if stack: # try to get the operation
                            op = stack.pop()
                        if op  == "+":
                            acc += val
                        elif op == "-":
                            acc -= val
                        elif op == "(":
                            acc += val
                            break # means that we are done with "("
                    # we append this acc to our stack again
                    stack.append(acc)
        if num:
            stack.append(int(num))
#        print (stack)
        # we pop our stack and put into our res
        while True:
            val = stack.pop()
            op = None
            if stack: # try to get the operation
                op = stack.pop()
            if op  == "+":
                res += val
            elif op == "-":
                res -= val
            elif op == None:
                res += val
            if not stack:
                break
                
        return res
solution = Solution()
string ="1+1"
print (solution.calculate(string))