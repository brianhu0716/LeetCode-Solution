# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:16:22 2021

@author: Brian
"""
'''
座標(i,j)-->當前硬幣面額為i，欲組出的數字為j。
當前座標(i,j)有兩種可能，第一是不拿當前面額的硬幣，所以值應為座標(i - 1,j)的值；第二種可能為拿當錢面額的硬幣一個加上當前要拿的
金錢減去當前硬幣面額所需的最少硬幣數(dp[i][j - coins[i]] + 1，加1代表當前面額硬幣一個)
*** 本題因為是要回傳兩種可能的最小值，因此只要超出邊界的值都要回傳無限大
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.insert(0,0)
        l = len(coins)
        self.dp = [[-1 for money in range(amount + 1)] for coin in range(l)]
        #print(self.dp)
        def mycoinChange(i,j):
            #print(i,j)
            if j < 0 : return float('inf') # 組成負數的錢(不存在)
            if j == 0 : return 0 # 任一面額的硬幣組成0元-->需要0個
            if i == 0: return float('inf') # 0元組成任意數量的錢都需要無限多個
            if self.dp[i][j] != -1:return self.dp[i][j]
            
            res = min(mycoinChange(i - 1,j),1 + mycoinChange(i,j - coins[i]))
            self.dp[i][j] = res
            
            #print(self.dp)
            
            return res
        
        ans = mycoinChange(l - 1,amount)
        return ans if ans != float('inf') else -1