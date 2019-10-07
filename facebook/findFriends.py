# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:40:39 2019

@author: huyn
"""

#Given the CSV with the belowing information :
#StartTime,user1,user2,action

#There are 4 possible actions : REQUEST,ACCEPT,REJECT,REMOVE
#REMOVE is only possible when users already be friend.
#
#Going through the csv, determine the list of users who are friends.
import csv
def findFriends(csvFile):
    data,users = readCSV(csvFile)
    graph      = makeGraph(data,users)
    res        = []
    for user1 in users:
        temp =[user1]
        for user2 in users:
            if graph[user1][user2] == "F":
                temp.append(user2)
        res.append(temp)
    return res 
def readCSV(csvFile):
    res = []
    users = set()
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            res.append(row)
            users.add(row[0])
            users.add(row[1])
    return sorted(res,key = lambda x:x[0]),users

def makeGraph(data,users):
    d ={}
    for user1 in users:
        for user2 in users:
            d[user1][user2]= ""
    for time,user1,user2,action in data:
        if action == "REQUEST":
            d[user1][user2]="R"
        elif action=="ACCEPT":
            # only make friend if user1 requested user2
            if d[user2][user1]=="R":
                d[user1][user2]="F"
                d[user2][user1]="F"
        elif action=="REJECT":
            if d[user2][user1]=="R":
                d[user1][user2]=""
                d[user2][user1]=""
        elif action == "REMOVE":
            if d[user1][user2]=="F":
                d[user1][user2]==""
                d[user2][user1]==""
    return d

