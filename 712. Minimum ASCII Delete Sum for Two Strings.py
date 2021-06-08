# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:47:22 2021

@author: Brian
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def helper(s1,s2):
            if (s1,s2) in self.d.keys(): return self.d[(s1,s2)]
            
            if not s1 : return sum([ord(word) for word in s2])
            
            if not s2 : return sum([ord(word) for word in s1])
            
            if s1[-1] == s2[-1]:
                ans = helper(s1[:-1],s2[:-1])
            else:
                ans = min(ord(s1[-1]) + helper(s1[:-1],s2),ord(s2[-1]) + helper(s1,s2[:-1]))
              
            self.d[(s1,s2)] = ans
            
            return ans
        
        self.d = dict()
        
        return helper(s1,s2)