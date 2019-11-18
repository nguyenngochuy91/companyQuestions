# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:23:36 2019

@author: huyn
"""
"""
You are given with a string . Your task is to remove atmost two substrings of any 
length from the given string such that the remaining string contains vowels('a','e','i','o','u') only. 
Your aim is the maximise the length of the remaining string. Output the length of remaining string after 
removal of atmost two substrings.
NOTE: The answer may be 0, i.e. removing the entire string.
Sample Input
2
earthproblem
letsgosomewhere
Sample Output
3
2
"""
def solve(numRouters,numLinks,links):
    time = 0
    graph = {}
    routers = set()
    for start,stop in links:
        if start not in graph:
            graph[start] = []
        if stop not in graph:
            graph[stop] = []
        graph[start].append(stop)
        graph[stop].append(start)
        routers.add(start)
        routers.add(stop)
    visited = {r:False for r in routers}    
    discoveryTime = {r:float("inf") for r in routers}
    trace = {r:float("inf") for r in routers}
    parents = {r:-1 for r in routers}
    ap =  {r:False for r in routers} 
    print (graph,routers)
    def dfs(router):
        children = 0
        visited[router] = True
        nonlocal time
        trace[router] = time
        discoveryTime[router] = time
        time+=1
        
        for nei in graph[router]:
            if not visited[nei]:
                children+=1
                parents[nei] = router
                dfs(nei)
                trace[router] = min(trace[router],trace[nei])
                
                if parents[router] == -1 and children >=2:
                    ap[router] = True
                if parents[router]!=-1 and trace[router] >= discoveryTime[router]:
                    ap[router] = True
            elif router!= parents[nei]:
                trace[router] = min(trace[router],trace[nei])
    for router in routers:
        if not visited[router]:
            dfs(router)
    print (ap)
    return [router for router in routers if ap[router]]

print (solve(6,5, [[1,2],[2,3],[3,4],[4,5],[6,3]]))
    