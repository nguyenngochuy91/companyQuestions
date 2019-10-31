# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:15:44 2019

@author: huyn
"""
"""
348. Design Tic-Tac-Toe
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game."""
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.player = {1:{"r":{i:0 for i in range(n)},"c":{i:0 for i in range(n)},"t":0,"b":0},
                        2:{"r":{i:0 for i in range(n)},"c":{i:0 for i in range(n)},"t":0,"b":0}}
        self.n = n
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        self.player[player]["r"][row] += 1
        self.player[player]["c"][col] += 1
        if self.player[player]["r"][row] == self.n or self.player[player]["c"][col] == self.n:
            return player
        # check for l, r
        if row == col:
            self.player[player]["t"] += 1
            if self.player[player]["t"] == self.n:
                return player
        if row + col ==self.n-1:
            self.player[player]["b"] += 1
            if self.player[player]["b"] == self.n:
                return player
        return 0
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)