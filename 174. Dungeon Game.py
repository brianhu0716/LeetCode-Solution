# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:16:18 2021

@author: Brian Hu
"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[0]*m for _ in range(n)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1]) 
        for i in range(n-2,-1,-1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])
        for i in range(m-2,-1,-1):
            dp[-1][i] = max(1, dp[-1][i+1] - dungeon[-1][i])
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]