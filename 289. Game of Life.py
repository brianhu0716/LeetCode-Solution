# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:06:23 2021

@author: brian.hu
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def defineState(i,j,board,m,n) :
            nlive = 0
            for x,y in [(i - 1,j),(i,j - 1),(i + 1,j),(i,j + 1),(i - 1,j - 1),(i + 1,j - 1),
                       (i - 1,j + 1),(i + 1,j + 1)] :
                if (0 <= x < m) and (0 <= y < n) and board[x][y] == 1 :
                    nlive += 1
            return nlive
        
        update = list()
        m,n = len(board),len(board[0])
        for x in range(m) :
            for y in range(n) :
                nlive = defineState(x,y,board,m,n)
                if board[x][y] == 0 and nlive == 3 :
                    update.append((x,y,1))
                if board[x][y] == 1 and (nlive < 2 or nlive > 3):
                    update.append((x,y,0))
        for x,y,val in update :
            board[x][y] = val
        
        return board