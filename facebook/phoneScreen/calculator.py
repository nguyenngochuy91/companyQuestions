# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:39:08 2019

@author: huyn
"""

def calculator():
    nums = 0
    operations = "+-="
    accumulate = None
    lastOp =None
    while True:
        char = input("Please type in your input:")
        if char in operations:
            if not lastOp:
                lastOp = char
                # store accumulate as our our num
                if accumulate==None:
                    accumulate = nums
            else:
                if lastOp=="+":
                    accumulate+=nums
                elif lastOp=="-":
                    accumulate-=nums
                # print out to screen, basically do a lazy evaluation ehre
                print (accumulate)
                # check if is not equal, then we store as lastOp
                if char!="=":
                    lastOp= char
            # we reset our nums after every operation
            nums = 0
        else: # we store first num into accumulate
            nums= nums*10+int(char)
calculator()
            