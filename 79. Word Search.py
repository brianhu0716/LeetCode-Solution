# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:22:24 2021

@author: Brian
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(row,col,board,word,m,n,idx):
            if idx == len(word) : return True 
            
            if not (0 <= row < m) or not (0 <= col < n) or not board[row][col] or board[row][col] != word[idx] : 
                return False
            
            board[row][col] = False
            
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                if helper(row + dx, col + dy, board, word, m, n, idx + 1) : return True
            
            board[row][col] = word[idx]

            
        
        m,n = len(board),len(board[0])
        for row in range(m):
            for col in range(n):
                if helper(row, col, board, word, m, n, 0) : return True

        return False