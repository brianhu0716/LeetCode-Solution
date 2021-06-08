# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:03:39 2021

@author: Brian
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,x,y,m,n):
            if not (0 <= x < m) or not(0 <= y < n) : return 0
            
            if grid[x][y] == 0 or grid[x][y] == 2 : return 0
            
            grid[x][y] = 2
            
            return 1 + dfs(grid,x - 1,y,m,n) + dfs(grid,x + 1,y,m,n) + dfs(grid,x,y - 1,m,n) + dfs(grid,x,y + 1,m,n)
            
                       
        m,n = len(grid),len(grid[0])
        max_area = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    max_area = max(max_area,dfs(grid,row,col,m,n))

        return max_area