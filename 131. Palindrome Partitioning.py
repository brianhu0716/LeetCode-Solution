# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:44:31 2021

@author: brian.hu
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(start):
            if start in self.memo : 
                return self.memo[start]
            if start == ls : 
                return [[]]
            
            ans = list()
            for end in range(start + 1,ls + 1) :
                if s[start : end] == s[start : end][::-1] :
                    ans = ans + list(map(lambda x : [s[start : end]] + x ,dfs(end)))
            self.memo[start] = ans
            return ans
        
        self.memo = dict()
        ls = len(s)
        return dfs(0)