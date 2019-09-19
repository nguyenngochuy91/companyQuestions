# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:05:08 2019

@author: huyn
"""

#721. Accounts Merge
#Given a list accounts, each element accounts[i] is a list of strings, where the first element 
#accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
#
#Now, we would like to merge these accounts. Two accounts definitely belong to the 
#same person if there is some email that is common to both accounts. Note that even if
# two accounts have the same name, they may belong to different people as people could have the same name. 
# A person can have any number of accounts initially, but all of their accounts definitely have the same name.
#
#After merging the accounts, return the accounts in the following format: the first 
#element of each account is the name, and the rest of the elements are emails in sorted order. 
#The accounts themselves can be returned in any order.
def accountsMerge(accounts):
    return