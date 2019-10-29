# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 01:09:22 2019

@author: huyn
"""
"""
332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the 
smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] 
has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary."""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        for x,y in tickets:
            if x not in graph:
                graph[x] = {}
            if y not in graph[x]:
                graph[x][y] = 0
            # count of how many of this we can use
            graph[x][y] += 1
        self.res = ""
        def dfs(currentPath,currentPoint):
            if len(currentPath) == len(tickets)+1:
                string = ",".join(currentPath)
                if not self.res:
                    self.res = string
                else:
                    self.res = min(self.res,string)
                return True
            else:
                if currentPoint in graph:
                    for neighbor in sorted(graph[currentPoint]):
                        if graph[currentPoint][neighbor]!= 0:
                            graph[currentPoint][neighbor]-=1
                            currentPath.append(neighbor)
                            check = dfs(currentPath,neighbor)
                            graph[currentPoint][neighbor]+=1
                            currentPath.pop()
                            if check:
                                return True
                return False
        dfs(["JFK"],"JFK")
        return self.res.split(",")
    
solution = Solution()
tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print (solution.findItinerary(tickets))
expected = ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]