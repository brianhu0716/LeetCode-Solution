# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:00:00 2021

@author: Brian
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col,m,n,board):

            if board[row][col] == "X" or board[row][col] == "D" : return 
            
            board[row][col] = "D"
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                if (0 < row + dx < m) and (0 < col + dy < n):                    
                    dfs(row + dx,col + dy,m,n,board)
            
            return 

        m,n = len(board),len(board[0])
        for row in range(m):
            for col in range(n):
                if (row != 0 or row != m - 1) and (col == 0 or col == n - 1) :
                    if board[row][col] == "O" :
                        dfs(row,col,m,n,board)
                elif (row == 0 or row == m - 1) :
                    if board[row][col] == "O": 
                        dfs(row,col,m,n,board)
                

        for row in range(m):
            for col in range(n):
                if board[row][col] == "D" :
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"