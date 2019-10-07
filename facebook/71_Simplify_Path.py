# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:27:25 2019

@author: huyn
"""

#71. Simplify Path
#Given an absolute path for a file (Unix-style), simplify it. Or in other words,
# convert it to the canonical path.
#
#In a UNIX-style file system, a period . refers to the current directory. Furthermore, 
#a double period .. moves the directory up a level. For more information, see: 
#    Absolute path vs relative path in Linux/Unix
#
#Note that the returned canonical path must always begin with a slash /, and there 
#must be only a single slash / between two directory names. The last directory name 
#(if it exists) must not end with a trailing /. Also, the canonical path must be the shortest 
#string representing the absolute path.
def simplifyPath(self, path: str) -> str:
    path = [item for item in path.split("/") if item!=""]
    stack = []
    for item in path:
        if item ==".":
            continue
        elif item == "..":
            if stack:
                stack.pop()
        else:
            stack.append(item)
    if not stack:
        return "/"
    return "/"+"/".join(stack)
