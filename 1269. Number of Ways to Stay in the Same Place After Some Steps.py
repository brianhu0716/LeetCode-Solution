# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:56:59 2021

@author: brian.hu
"""
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        '''
        mod = 10 ** 9 + 7
        dp = [0 for i in range(arrLen + 2)]
        state = [0 for i in range(arrLen + 2)]
        n = len(dp)
        dp[1] = 1
        for step in range(1,steps + 1) :
            for i in range(1,n - 1) :
                state[i] = (dp[i - 1] + dp[i] + dp[i + 1]) % mod 
            dp = state[:]
            
        return dp[1]
        '''
        
        mod = 10 ** 9 + 7
        def helper(idx,left) :
            if (idx,left) in self.memo : return self.memo[(idx,left)]
            
            if left == 0 : return 1 if idx == 0 else 0
            
            if idx == arrLen - 1 : # 只能留在原地或往左
                ans = helper(idx - 1,left - 1) + helper(idx,left - 1)
            elif idx == 0 : # 只能留在原地或往右
                ans = helper(idx + 1,left - 1) + helper(idx,left - 1)
            else : # 可以留在原地或往左或往右
                ans = helper(idx + 1,left - 1) + \
                        helper(idx,left - 1) + helper(idx - 1,left - 1)
            self.memo[(idx,left)] = ans % mod
            return self.memo[(idx,left)]
        
        self.memo = dict()

        return helper(0,steps)