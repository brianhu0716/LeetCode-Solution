# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:20:19 2021

@author: brian.hu
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def helper(idxs,idxt,res) :
            if (idxs,idxt) in self.memo : 
                return self.memo[(idxs,idxt)]
            if res == t : # 找到一個答案
                return 1
            if idxs == len(s) or idxt == len(t) : # 超出s或t的邊界但沒找到答案
                return 0
            
            if s[idxs] == t[idxt] : # 如果當前s以及t指標到的字相同，可以選擇拿或不拿
                ans = helper(idxs + 1,idxt + 1,res + s[idxs]) + helper(idxs + 1,idxt,res)
            else : # 如果當前s以及t指標到的字不同，只能選擇不拿
                ans = helper(idxs + 1,idxt,res)
            self.memo[(idxs,idxt)] = ans
            return ans
        
        self.memo = dict()
        return helper(0,0,"")
