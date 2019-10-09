# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 01:30:16 2019

@author: huyn
"""

#680. Valid Palindrome II
#Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
def validPalindrome(s: str) -> bool:
    start ,stop = 0,len(s)-1
    def dfs(s,start,stop,count):
        if start == stop:
            return True
        elif start+1==stop:
            if s[start]==s[stop]:
                return True
            else:
                return count == 0
        elif start<stop:
            if s[start]==s[stop]:
                return dfs(s,start+1,stop-1,count)
            else:
                if count>0:
                    return False
                else:
                    return dfs(s,start+1,stop,1) or dfs(s,start,stop-1,1)
    return dfs(s,start,stop,0)

def validPalindromeI(s: str) -> bool:
    start ,stop = 0,len(s)-1
    count = 0
    
    return dfs(s,start,stop,0)