# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:02:48 2021

@author: Brian
"""

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1 : return 0
        
        def helper(now,hold): # 
            if (now,hold) in self.memo.keys() : return self.memo[(now,hold)] # memoization
            if now > n: return float('inf') # out of bound
            
            if now == n : return 0 # find the target
			
			# we can only paste with one operation or paste then copy with two operations
            ans = min(1 + helper(now + hold,hold),2 + helper(now + hold,now + hold)) 

            self.memo[(now,hold)] = ans
            
            return ans
                          
        self.memo = dict()
        return 1 + helper(1,1) # initially, we have 1 "A" and can only copy "A" with one operation
