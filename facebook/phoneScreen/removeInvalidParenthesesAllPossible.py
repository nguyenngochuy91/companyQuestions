# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:14:59 2019

@author: huyn
"""

#301. Remove Invalid Parentheses
#Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
#Note: The input string may contain letters other than the parentheses ( and ).
def removeInvalidParentheses(s: str):
   # find misplace left and right
    right = 0
    left = 0
    correct =0
    for item in s:
        if item=="(":
            left+=1
        elif item==")":
            if left>0:
                left-=1
                correct+=1
            elif left==0:
                right+=1
    res = set()
    def dfs(left,right,currentList,index,correctLeft,correctRight):
        # when index is equal to length of s, we have 1 solution
        if index==len(s):
#            print (30,left,right,currentList,index,correctLeft,correctRight)
            res.add("".join(currentList))
        elif index<len(s):
            currentChar = s[index]
#            print (37,currentChar,left,right,currentList,index,correctLeft,correctRight)
            if currentChar == "(":
                # we check if we can ignore this
                if left>0:
                    # this means we can choose to skip this
                    dfs(left-1,right,currentList,index+1,correctLeft,correctRight)
                # we will include it if and only if correctLeft greater than 0
                if correctLeft>0:
                    currentList.append("(")
                    dfs(left,right,currentList,index+1,correctLeft-1,correctRight)
                    currentList.pop()
            elif currentChar==")":
                if right>0:
#                    this means we can choose to skip this
                    dfs(left,right-1,currentList,index+1,correctLeft,correctRight)
                if correctRight>0 and correctLeft<correctRight: # make sure what we have is still valid
                    currentList.append(")")
                    dfs(left,right,currentList,index+1,correctLeft,correctRight-1)
                    currentList.pop()
            else:
                currentList.append(currentChar)
                dfs(left,right,currentList,index+1,correctLeft,correctRight)
                currentList.pop()
    dfs(left,right,[],0,correct,correct)
    return list(res)
s= "(a)())()"
print (removeInvalidParentheses(s))
s ="(a)())()"