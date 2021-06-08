# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:57:06 2021

@author: Brian
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            
            if self.grid[row][col] == "2" or self.grid[row][col] == "0" : return 
            
            self.grid[row][col] = "2"
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                if (0 <= row + dx < len(self.grid)) and (0 <= col + dy < len(self.grid[0])) :
                    dfs(row + dx,col + dy)
            
            return 
        
        ans = 0
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == "1":
                    ans += 1
                    dfs(row,col)
                    #print(self.grid)
        return ans