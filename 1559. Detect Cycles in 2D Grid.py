# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:33:53 2021

@author: Brian Hu
"""

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(i, j, pi, pj):
            self.visited[i][j] = True # record the position that has been walked through
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] != grid[i][j]:
                    continue
                if self.visited[x][y]:
                    if (x, y) != (pi, pj): # current position is visited but not the same as previous position 
                        self.flag = True
                        return 
                else:
                    dfs(x, y, i, j)

                    
        self.visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.flag = False
        for i in range(m := len(grid)):
            for j in range(n := len(grid[0])):
                if not self.visited[i][j]: # if the position iss visited, it must can form a cycle
                    dfs(i, j, -1, -1)
                    if self.flag: return True
        return False