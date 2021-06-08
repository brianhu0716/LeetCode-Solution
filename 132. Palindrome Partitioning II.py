# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:48:27 2021

@author: brian.hu
"""

class Solution(object):
    def minCut(self, s):
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0
        for j in range(1, len(s)+1):
            for i in range(j):
                if dp[i] != float('inf') and s[i:j] == s[i:j][::-1]:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1] - 1