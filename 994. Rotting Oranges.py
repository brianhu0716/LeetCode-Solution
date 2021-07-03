# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:32:34 2021

@author: Brian Hu
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans, fresh = 0, 0 # ans is the minima time we need to cost to rotten all fresh orange, fresh is the fresh oranges in initial state
        rot = deque()
        for i in range(m := len(grid)):
            for j in range(n := len(grid[0])):
                if grid[i][j] == 2:
                    rot.append((i, j))
                    grid[i][j] = 3
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0: 
            return 0
        while rot and fresh: # if there is no any orange in the moment still fresh, we can stop BFS since the rotten orange can't have chance to  contaminate any other FRESH orange.  
            for cnt in range(len(rot)):
                i, j = rot.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)): # every rotten orange can cause its 4-direction fresh orange rotten
                    if (0 <= x < m) and (0 <= y < n) and grid[x][y] == 1: # another fresh orange is rotten
                        fresh -= 1
                        grid[x][y] = 3 # label the rotten orange we've already used 
                        rot.append((x,y)) # push new rotten orange into deque
            ans += 1
        if fresh != 0: # still have fresh oranges
            return -1
        return ans