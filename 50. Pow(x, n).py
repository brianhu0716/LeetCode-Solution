# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:28:35 2021

@author: Brian
"""
'''

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:    
        def mypow(x,k):
            if k in self.d.keys(): 
                return self.d[k]
            
            if k == 0: 
                return 1
       
            if k % 2 == 1 : 
                temp = x * mypow(x,k - 1)            
            else:
                temp = mypow(x,k // 2) * mypow(x,k // 2) 
                
            self.d[k] = temp
            return temp
        
        if n == 0: return 1
        if n < 0 : 
            x = 1 / x
            n = abs(n)
            
        self.d = {}
        if n % 2 == 1:
            return  x * mypow(x,n - 1)
        else:
            return mypow(x,n // 2) * mypow(x,n // 2)