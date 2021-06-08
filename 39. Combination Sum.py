# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 21:31:45 2021

@author: Brian
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.insert(0,0)
        dp = [[[] for amount in range(target + 1)] for coin in candidates]
        for row,coin in enumerate(candidates):
            if row == 0 : continue
            for amount in range(target + 1):
                if dp[row - 1][amount] : dp[row][amount] += dp[row - 1][amount]
                if amount - coin > 0:
                    if dp[row][amount - coin] :
                        for comb in dp[row][amount - coin]:
                            dp[row][amount] += [comb + [coin]]
                elif coin == amount: dp[row][amount] += [[coin]]
                else: continue                    
        return dp[-1][-1]