# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:05:36 2021

@author: brian.hu
"""

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def recursion(a,n) :
            if n in self.memo : return self.memo[n]
        
            if n == 0 : return 1
            
            if n % 2 == 0 :
                ans = recursion(a,n // 2) * recursion(a,n // 2)
            else :
                ans = a * recursion(a,n - 1)
            
            self.memo[n] = ans
            return ans
        
        num = 0
        digit = 0
        for n in b[::-1] :
            num += n * 10 ** digit
            digit += 1
        
            
        self.memo = dict()
        
        return recursion(a,1140 + num % 1140) % 1337
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             