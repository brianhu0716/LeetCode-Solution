# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:55:46 2021

@author: brian.hu
"""
"""
對於任一數字，我們考慮把它再減去一個使其剩餘之數大於0的所有可能，當減到0後，我們return 1，
並計算該數字的所有拆解後成績最大的值，並記錄該值已備之後須要用到
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        def dfs(n_now) :
            if n_now in self.memo : return self.memo[n_now]
            if n_now == 0 : return 1

            ans = float('-inf')
            for i in range(1,n) :
                if n_now - i >= 0 :
                    ans = max(ans,i * dfs(n_now - i))
            self.memo[n_now] = ans
            return ans
        
        self.memo = dict()
        return dfs(n)