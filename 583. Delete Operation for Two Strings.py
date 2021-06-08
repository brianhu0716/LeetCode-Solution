# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:34:22 2021

@author: Brian
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(s1,s2):
            if (s1,s2) in self.d.keys(): return self.d[(s1,s2)]
            
            if not s1 : return len(s2)
            
            if not s2 : return len(s1)
        
            if s1[-1] == s2[-1]:
                ans = helper(s1[:-1],s2[:-1])
            else:
                ans = 1 + min(helper(s1[:-1],s2),helper(s1,s2[:-1]))
                
            self.d[(s1,s2)] = ans
            
            return ans
        
        self.d = {}
        
        return helper(word1,word2)