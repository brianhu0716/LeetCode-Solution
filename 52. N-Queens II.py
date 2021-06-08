# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:26:20 2021

@author: brian.hu
"""
# 與51題相同
class Solution:
    def totalNQueens(self, n: int) -> int:
        def checkValid(row,col,res):
            for place in res:
                x,y = place[0],place[1]
                if x == row or y == col or abs(x - row) == abs(y - col):
                    return False
            return True
        
        def dfs(row,res):
            if row == n:
                self.ans += 1
                return 
            
            for col in range(n):
                if checkValid(row,col,res):
                    dfs(row + 1,res + [(row,col)])
                    
            return         
            
        self.ans = 0
        dfs(0,list())
        return self.ans