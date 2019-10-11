# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:50:19 2019

@author: Huy Nguyen
"""

# valid ip address
def validIPAddress (IP: str) -> str:
    if isIP4(IP):
        return "IPv4"
    if isIP6(IP):
        return "IPv6"
    return "Neither"
     
def isIP4(string):
    string = string.split(".")
    if len(string)!=4:
        return False
    for item in string:
        if len(item)==1:
            continue
        else:
            check = True
            if item.isdigit():
                check= (item[0]!="0" and int(item)<256)
            else:
                return False
            if not check:
                return False
    return True
def isIP6(string):
    string = string.split(":")
    if len(string)!=8:
        return False
    for item in string: 
        if item==0:
            if len(item)>1:
                if item[0]=="0":
                    return False
        if len(item)>4:
            return False
        if len(item)==1:
            if item.isalpha():
                if item.lower()>"f":
                    return False
        elif len(item)>1:
            for l in item:
                if l.isalpha():
                    if l.lower()>"f":
                        return False
                elif l.isdigit():
                    continue
                else:
                    return False
        else:
            return False
        
    return True

#IP = "172.16.254.1" ->True
#IP = "g:f:f:f:f:f:f:g" ->False
#IP = "02001:0db8:85a3:0000:0000:8a2e:0370:7334" ->False
#IP = "2001:db8:85a3:0:0:8A2E:0370:7334" ->True

