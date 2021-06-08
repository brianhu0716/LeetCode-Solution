# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:43:33 2021

@author: Brian
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(idx,s):
            if idx == len(s) : return 1
            
            if (idx,s[idx]) in self.d.keys() : return self.d[(idx,s[idx])]
            
            
            if s[idx] == "0" : return 0
            
            if  s[idx:idx + 2] > "26" or idx == len(s) - 1:  
                res1 = 1 * helper(idx + 1,s)          

            else:
                res1 = 1 * helper(idx + 1,s) + 1 * helper(idx + 2,s)
                
            self.d[(idx,s[idx])] = res1
                
            return res1
            
        self.d = dict()
        
        ans =  helper(0,s)
        
        return ans