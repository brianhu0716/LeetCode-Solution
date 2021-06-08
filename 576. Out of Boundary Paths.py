# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:58:13 2021

@author: Brian
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def helper(left_move,row,col,m,n):
            if (row,col,left_move) in self.d.keys() : return self.d[(row,col,left_move)]
            
            if row > m or col > n or row < 0 or col < 0 : return 1
            
            if left_move == 0 : return 0
            
            ans = helper(left_move - 1,row - 1,col,m,n) + helper(left_move - 1,row + 1,col,m,n) + \
                    helper(left_move - 1,row,col - 1,m,n) + helper(left_move - 1,row,col + 1,m,n)
            
            self.d[(row,col,left_move)] = ans
            
            return ans
        
        self.d = dict()
        
        return helper(maxMove,startRow,startColumn,m - 1,n - 1)  % 1000000007