# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:58:34 2021

@author: brian.hu
"""

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        def helper(n,left) :
            if (n,left) in self.dp : return self.dp[(n,left)] 
            if left == 0 :  # 找到target，如果剛好用了d個骰return True 否則False
                return 1 if n == 0 else 0
            if n == 0 or left < 0 : return 0 # 沒有骰子可以拿或是拿到超過target
            
            ans = 0
            for num in range(1,f + 1) : # 當前狀態可以選擇1~f + 1之間的一個數字
                ans += helper(n - 1,left - num) 
            self.dp[(n,left)] = ans % mod
            return self.dp[(n,left)]
        self.dp = dict()
        return helper(d,target)