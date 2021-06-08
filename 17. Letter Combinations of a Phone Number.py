# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:25:05 2021

@author: Brian
"""

class Solution:
    def __init__(self):
        self.d = {
                  "2" : ["a","b","c"],
                  "3" : ["d","e","f"],
                  "4" : ["g","h","i"],
                  "5" : ["j","k","l"],
                  "6" : ["m","n","o"],
                  "7" : ["p","q","r","s"],
                  "8" : ["t","u","v"],
                  "9" : ["w","x","y","z"]
                    }
        
        self.ans = []
        self.res = ""
        
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx,digits):
            if idx == len(digits) : return 

            
            num = digits[idx]
            for char in self.d[num]:
                self.res += char
                dfs(idx + 1,digits)
  
                if len(self.res) == len(digits) : self.ans += [self.res] 

                self.res = self.res[:-1]
                #print(self.ans)
       
        dfs(0,digits)
        
        return self.ans