# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:16:05 2021

@author: Brian
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stack = []
        for price in prices:
            if not stack: 
                stack.append(price)
            else:
                if price < stack[-1]:
                    stack.append(price)
                else:
                    max_profit = max(max_profit,price - stack[-1])
        return max_profit