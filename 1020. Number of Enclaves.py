# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:26:50 2021

@author: Brian Hu
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid):    
            grid[i][j] = -1
            self.cnt += 1
            for x, y in ((i + 1, j), (i, j + 1), (i, j - 1), (i - 1, j)):
                if not (0 <= x < m) or not (0 <= y < n):
                    self.reach = True # this block can reach sea
                    continue
                if grid[x][y] != -1 and grid[x][y] == 1:
                    dfs(x, y, grid)
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.reach = False
                    self.cnt = 0
                    dfs(i, j, grid)
                    if not self.reach:
                        ans += self.cnt
        return ans