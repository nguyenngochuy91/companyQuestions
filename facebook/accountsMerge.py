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
    graphs= {}
    for account in accounts:
        name = account[0]
        if name not in graphs:
            graphs[name] ={"vertex":set(),"edges":{}}
        # we create a graph using the emails
        emails = account[1:]
        if len(emails)==1:
            graphs[name]["vertex"].add(emails[0])
        for i in range(len(emails)-1):
            email1 = emails[i]
            graphs[name]["vertex"].add(email1)
            for j in range(i+1,len(emails)):
                email2 = emails[j]
                if email1 not in graphs[name]["edges"]:
                    graphs[name]["edges"][email1]=[]
                if email2 not in graphs[name]["edges"]:
                    graphs[name]["edges"][email2]=[]                   
                graphs[name]["edges"][email1].append(email2)
                graphs[name]["edges"][email2].append(email1)
        graphs[name]["vertex"].add(emails[-1])
    output = []
    # def dfs function
    def dfs(currentNode):

        path =[currentNode]
#        print (47,currentNode)
        if currentNode in edges:
            for neighbor in edges[currentNode]:
                if not visited[neighbor]:
#                    print (51,neighbor)
                    visited[neighbor] = True
                    path.extend(dfs(neighbor))
        return path
    # using dfs to find connected component for each name
    for name in graphs:
        edges,vertices = graphs[name]["edges"],graphs[name]["vertex"]
        cc           = []
        visited      = {vertex:False for vertex in vertices}
        for vertex in vertices:
            if not visited[vertex]:
                visited[vertex] = True
#                print (vertex)
                cc.append(dfs(vertex))
        for component in cc:
            temp = [name]
            temp.extend(sorted(component))
            output.append(temp)
    return output
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print (accountsMerge(accounts))


    