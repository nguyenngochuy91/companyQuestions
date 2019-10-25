# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:05:08 2019

@author: huyn
"""
import collections
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
    em_to_name = {}
    graph = collections.defaultdict(set) # create a graph that store infor of emails that are unique
    # this graph would help us to do connected components later
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            # we dont need an edge between every pair of edge, just add edge between first to every other
            # and everyother to first, then later on, if appear an edge to another different email
            # we can still join them together
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            # link the email back to the name
            em_to_name[email] = name 

    seen = set()
    ans = []
    for email in graph:
        # we do a connected component search here
        if email not in seen:
            # we add this email to seen
            seen.add(email)
            # initiate a stack for our component
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            # done w stack means we have connected all possible that link to the email, using the map to name 
            # to create an entry in answer
            ans.append([em_to_name[email]] + sorted(component))
    return ans
#accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
#print (accountsMerge(accounts))


    