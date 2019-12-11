# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:00:12 2019

@author: huyn
"""
# top down
def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for i in range(capacity+1)] for j in range(len(profits))]
    return solve_knapsack_recursive(dp,profits,weights,capacity,0)
def solve_knapsack_recursive(dp,profits,weights,capacity,currentIndex):
    # base condition
    if capacity<=0 or currentIndex>=len(weights):
        return 0
    if dp[currentIndex][capacity]!= -1:
        return dp[currentIndex][capacity]
    profit1 = 0
    
    if weights[currentIndex] <=capacity:
        profit1 = profits[currentIndex] + solve_knapsack_recursive(dp,profits,weights,capacity-weights[currentIndex],currentIndex+1)
    profit2 = solve_knapsack_recursive(dp,profits,weights,capacity,currentIndex+1)
    dp[currentIndex][capacity] = max(profit1,profit2)
    return dp[currentIndex][capacity]
print (solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

# bottom up
def solve_knapsack1(profits, weights, capacity):
  # basic checks
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(n)]

  # populate the capacity = 0 columns, with '0' capacity we have '0' profit
  for i in range(0, n):
    dp[i][0] = 0

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      # exclude the item
      profit2 = dp[i - 1][c]
      # take maximum
      dp[i][c] = max(profit1, profit2)

  # maximum profit will be at the bottom-right corner.
  print(dp)
  return dp[n - 1][capacity]
  
def solve_knapsack2(profits, weights, capacity):
  # basic checks
  n = len(profits)
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [0 for x in range(capacity+1)]

  # if we have only one weight, we will take it if it is not more than the capacity
  for c in range(0, capacity+1):
    if weights[0] <= c:
      dp[c] = profits[0]

  # process all sub-arrays for all the capacities
  for i in range(1, n):
    for c in range(capacity, -1, -1):
      profit1, profit2 = 0, 0
      # include the item, if it is not more than the capacity
      if weights[i] <= c:
        profit1 = profits[i] + dp[c - weights[i]]
      # exclude the item
      profit2 = dp[c]
      # take maximum
      dp[c] = max(profit1, profit2)

  return dp[capacity]