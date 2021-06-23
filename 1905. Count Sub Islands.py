# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:28:08 2021

@author: Brian Hu
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):    
            if grid1[i][j] != 1: # if grid2[i][j] == 1 and grid1[i][j]  != 1, the island in grid2 is not the sub-island of grid1
                self.flag = False
            grid2[i][j] = -1 # labeling the path we've walked through
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (0 <= x < m) and (0 <= y < n) and grid2[x][y] not in (-1, 0): # next cordination must in grid and haven't been visited and can't be the water
                    dfs(x,y)
        
        m, n = list(map(lambda x: len(x), [grid2, grid2[0]]))
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.flag = True
                    dfs(i, j)
                    if self.flag: # the island in grid2 is sub-island of grid1
                        ans += 1
        return ans