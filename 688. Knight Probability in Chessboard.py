# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:30:00 2021

@author: Brian
"""

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def helper(n,moves_left,row,col):
            if (row,col,moves_left) in self.d.keys() : return self.d[(row,col,moves_left)]
            
            if not (0 <= row <= n) or not (0 <= col <= n): return 0
            
            if moves_left == 0 : return 1
            
            ans_now = 0
            for dx,dy in [[-2,1],[-2,-1],[2,1],[2,-1],[-1,2],[1,2],[-1,-2],[1,-2]] :
                ans_now += helper(n, moves_left - 1, row + dx, col + dy)
            
            self.d[(row,col,moves_left)] = ans_now
            
            return ans_now
            
        self.d = dict()
        return helper(n- 1,k,row,column) / 8 ** k