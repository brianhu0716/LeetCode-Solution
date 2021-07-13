# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:13:24 2021

@author: Brian Hu
"""

class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(n):
            if n in self.dp: return self.dp[n]
            
            if n == 1: return 0
            
            if n % 2 == 0:
                ans = 1 + helper(n // 2)
            else:
                ans = 1 + min(helper(n + 1), helper(n - 1))
            
            self.dp[n] = ans
            return ans
        
        self.dp = dict()
        return helper(n)