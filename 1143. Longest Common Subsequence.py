# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:16:24 2021

@author: Brian
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(s1,s2):
            if not s1 or not s2: return 0
            
            if (s1,s2) in self.d.keys(): return self.d[(s1,s2)]
            
            if s1[-1] == s2[-1]:
                ans = 1 + helper(s1[:-1],s2[:-1])
            else:
                ans = max(helper(s1[:-1],s2),helper(s1,s2[:-1]))
                
            self.d[(s1,s2)] = ans
            
            return ans
        
        self.d = {}    
        return helper(text1,text2)