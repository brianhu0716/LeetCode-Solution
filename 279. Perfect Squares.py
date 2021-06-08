# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:59:01 2021

@author: Brian
"""

class Solution:
    def __inti__(self):
        import math
    def numSquares(self, n: int) -> int:
        perfects = [i ** 2 for i in range(1,int(math.sqrt(n) + 1))]
        
        dp = [[0 for i in range(n + 1)] if perfect != 1 else [i for i in range(n + 1)] for perfect in perfects]
        
        for row in range(1,lp := len(perfects)):
            perfect = perfects[row]
            for target in range(n + 1):
                if target < perfect:
                    dp[row][target] = dp[row - 1][target]
                else :
                    dp[row][target] = min(dp[row - 1][target],1 + dp[row][target - perfect])
                    
        return min([dp[row][-1] for row in range(lp)])