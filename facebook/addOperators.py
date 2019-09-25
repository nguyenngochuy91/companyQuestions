# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:13:39 2019

@author: huyn
"""
import random
#282. Expression Add Operators
#Given a string that contains only digits 0-9 and a target value, return all 
#possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
def addOperators(num: str, target: int):
    arr = []
    def dfs(start,path,target,accumulate,prevVal):
#        print (path,accumulate)
        if start == len(num):
            if accumulate==target:  
                arr.append("".join(path))
        elif start<len(num):
#            print (path)
            for i in range(start,len(num)):
                string = num[start:i+1]
                # check if string is valid 
                if str(int(string))==string:  
                    try:
                        val    = int(string)
                    except:
                        val    = 0
                    path.append("+")
                    path.append(string)
                    dfs(i+1,path,target,accumulate+val,val)
                    path.pop()
                    path.pop() 
                    path.append("-")
                    path.append(string)
                    dfs(i+1,path,target,accumulate-val,-val)
                    path.pop()   
                    path.pop() 
                    path.append("*")
                    path.append(string)
                    pre = prevVal*val
                    dfs(i+1,path,target,accumulate-prevVal+pre,pre)
                    path.pop()  
                    path.pop() # pop trhe string
    for i in range(len(num)):
        string = num[:i+1]  
        if str(int(string))==string:                
            dfs(i+1,[string],target,int(string),int(string))
    return arr
#num ="12345"
#print (addOperators(num,4))
#target = 6
#num = "123"
#print (addOperators(num,target))
#target = 6
#num = "232"
#print (addOperators(num,target))
#target = 8
#num = "232"
#print (addOperators(num,target))
#target = 0
#num   = "00"
#print (addOperators(num,target))
for i in range(1):
    num = random.randint(1,10**6)
    target = random.randint(1,10)
    print (""""{}"\n{}""".format(num,target))