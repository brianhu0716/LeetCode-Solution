# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:01:13 2021

@author: brian.hu
"""
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        if (n := len(num)) < 3 : return []  # special case
        
        def dfs(start,res,n) :
            if start == n :
                if len(res) >= 3 : self.ans = res[:] # find answer
                #print(self.ans) # see answer you find
                return 
            
            for end in range(start + 1,n + 1) :
                if self.ans : continue # already find answer
                    
                if end - start > 1 and num[start : end][0] == "0" : continue # leading zero is invalid number
                
                if int(num[start : end]) >= 2 ** 31 : continue # each number can't exceed the 2 ** 31
                
                if len(res) < 2 :  # add the first two number
                    dfs(end,res + [int(num[start : end])],n)
                else :
                    if int(num[start : end]) == res[-1] + res[-2] : # chack whether the new number meets the definition of Finonacci sequence
                        dfs(end,res + [int(num[start : end])],n)
                
        self.ans = list()
        dfs(0,list(),n)
        return self.ans