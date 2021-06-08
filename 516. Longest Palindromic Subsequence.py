# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:25:10 2021

@author: Brian
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(s):
            if s in self.d.keys(): return self.d[s]
            
            if len(s) == 0: return 0
            
            if len(s) == 1: return 1
            
            if s[0] == s[-1]: 
                ans = 2 + helper(s[1:-1])
            else:
                ans = max(helper(s[1:]),helper(s[:-1]))
            
            self.d[s] = ans
            
            return ans
            
        self.d = dict()    
        return helper(s)