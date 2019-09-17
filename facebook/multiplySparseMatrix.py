# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:33:11 2019

@author: huyn
"""
import time
#311. Sparse Matrix Multiplication
#Given two sparse matrices A and B, return the result of AB.
#
#You may assume that A's column number is equal to B's row number.
def multiply( A, B):
    row = len(A)
    col = len(B[0])
    output = []
    d ={"R":set(),"C":set()}
    for r in range(row):
        temp = []
        for c in range(col):
            if r in d["R"]:
                temp = [0]*len(A[0])
                continue
            else:
                val = 0
                if c not in d["C"]:
                    val = 0
                    # do this to check whether to indicate whole row in A is 0 or whole col in B is 0
                    checkRow= False
                    checkCol= False
                    for k in range(len(A[0])):
                        if A[r][k]!=0 and B[k][c]!=0:
                            val+=A[r][k]*B[k][c]
                        if A[r][k]!=0:
                            checkRow= True
                        if B[k][c]!=0:
                            checkCol= True
                    if not checkRow:
                        d["R"].add(r)
                    if not checkCol:
                        d["C"].add(c)
                temp.append(val)
        output.append(temp)
    return output        
def multiplyNormal( A, B):
    row = len(A)
    col = len(B[0])
    output = []
    for r in range(row):
        temp = []
        for c in range(col):
            val = 0
#            for k in range()
            for k in range(len(A[0])):
                val+=A[r][k]*B[k][c]
            temp.append(val)
        output.append(temp)
    return output
A = [
  [ 1, 0, 0,1],
  [-1, 0, 3,1],
  [0,0,0,0],
  [1,-1,10,2]
]
B = [
  [ 7, 0, 0 ,0],
  [ 0, 0, 0 ,0],
  [ 0, 0, 1,0 ],
  [1,2,3,0]
]
start = time.time()
print (multiplyNormal(A,B))
stop = time.time()
print ((stop-start))
start = time.time()
print (multiply(A,B))
stop = time.time()
print ((stop-start))