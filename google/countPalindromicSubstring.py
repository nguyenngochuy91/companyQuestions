# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:31:00 2019

@author: Huy Nguyen
"""

# Count of Palindromic substring
def count_PS(st):

    n = len(st)
    # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0

  # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if st[startIndex] == st[endIndex]:
# if it's a two character string or if the remaining string is a palindrome too
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True
                    count += 1

    return count