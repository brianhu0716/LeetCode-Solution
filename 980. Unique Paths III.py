# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:48:29 2021

@author: Brian
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x,y,grid,seen):
            if grid[x][y] == -1 or seen[x][y]: #遇到障礙物或是已經走訪過
                return 
            if grid[x][y] == 2: # 到終點
                seen[x][y] = True # 已走訪終點座標
                #print(seen)
                if seen == standard: # 走過的路徑與標準答案相同
                    self.ans += 1
                seen[x][y] = False
                return
            
            seen[x][y] = True
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0 <= (next_x := x + dx) < m and 0 <= (next_y := y + dy) < n:  
                    dfs(next_x,next_y,grid,seen)
            seen[x][y] = False
            
        self.ans = 0
        m,n = len(grid),len(grid[0])
        standard = [[False if grid[x][y] == -1 else True for y in range(n)] for x in range(m)]
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    dfs(x,y,grid,[[False for _ in range(n)] for _ in range(m)])
                    return self.ans