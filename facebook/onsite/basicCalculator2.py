# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:29:09 2019

@author: huyn
"""
"""
227. Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and 
empty spaces . The integer division should truncate toward zero."""
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        acc = 0
        num = ""
        operation = ""
        s = s.replace(" ","")
        for letter in s:
            if letter.isdigit():
                num+= letter
            else:
                # this is an operation
                # check if we store an operation before
                if operation: # we have to evaluate it
                    # apparently we cant have 2 operations next to each other
                    # our num has to be valid
                    val = int(num)
                    # reset our num
                    num = ""
                    # if operation is + or -
                    if operation == "+":
                        res += val
                        acc = val
                    elif operation == "-":
                        res -= val
                        acc = -val
                    elif operation == "*":
                        # our last was a times
                        res -= acc
                        acc = acc*val
                        res += acc
                    elif operation == "/":
                        res -= acc
                        if acc<0:
                 
                            acc = - (abs(acc)//val)
                        else:
                            acc = acc//val
                        res += acc
                else:
                    # if there are no operation, this is our first  operation
                    # if we have a number before
                    if num:
                        val = int(num)
                        num = ""
                        # since we have no operation before, we just set our res and acc to this val
                        acc = val
                        res = val
                    # we have no num, basically this is just an operation
                operation = letter
        # we hit the end, we check our last operation
        if operation:
            val = int(num)
            # reset our num
            num = ""
            # if operation is + or -
            if operation == "+":
                res += val
                acc = val
            elif operation == "-":
                res -= val
                acc = -val
            elif operation == "*":
                # our last was a times
                res -= acc
                acc = acc*val
                res += acc
            elif operation == "/":
                res -= acc
                if acc<0:
        
                    acc = - (abs(acc)//val)
                else:
                    acc = acc//val
                res += acc
        else:
            # no operation, just astring of number
            res = int(num)
        return res
                        
                    
                    