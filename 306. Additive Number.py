# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:46:38 2021

@author: brian.hu
"""

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3 : return False # special case 
        
        def dfs(start,res) :
            if start == n and len(res) > 2 :
                self.find = True
                #print(res)
                return
            
            for end in range(start + 1,n + 1) :
                if self.find : continue # already find the answer
                    
                if end - start > 1 and num[start : end][0] == "0" : continue # leading zero is invalid number
                    
                if len(res) < 2 : # add the first two number 
                    dfs(end,res + [int(num[start : end])])
                else :
                    if int(num[start : end]) == res[-1] + res[-2] : # chack whether the new number meets the definition of additive number
                        dfs(end,res + [int(num[start : end])])
            
        
        self.find = False
        n = len(num)
        dfs(0,list())
        return self.find