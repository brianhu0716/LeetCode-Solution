# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:14:37 2021

@author: brian.hu
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(total,idx,n) :
            if (total,idx) in self.memo : return self.memo[(total,idx)]
            if total == 0 : return 1 # 找到一組目標
            if total < 0 or idx == n : return 0 # 超出邊界
            """
            對當前狀態總共有數字total，下一個狀態可以選擇拿當前的coin，也可以選擇不拿
            當前的coin。如果拿當前coin，idx不用加一，他的下一個狀態可以繼續選擇拿或不拿該
            coin；而不拿coin的話將idx + 1轉移到下一個狀態
            """
            ans = helper(total - coins[idx],idx,n) + helper(total,idx + 1,n)
            
            self.memo[(total,idx)] = ans
            
            return ans
        
        self.memo = dict()
        
        return helper(amount,0,len(coins))