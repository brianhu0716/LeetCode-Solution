# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:27:08 2021

@author: Brian
"""
'''
stack嚴格遞增，只要遇當前price比stack[-1]小，代表當前price是下一次買進的最好價格，在此之前必須把之前買的股票賣出，
最大獲利為stack[-1] 0 stack[0]，接著再把當前price放入stack中。
*** 為避免price為嚴格遞增或是尾部嚴格遞增，導致少算一次獲利，我們在結束前檢查stack中的數量，若大於2代表還可以在買進賣出一次
增加獲利，若只有一個，代表嚴格遞減，無法增加獲利

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = 0
        stack = list()
        for price in prices:
            if not stack:
                stack.append(price)
            else:
                if stack[-1] > price:
                    if len(stack) >= 2:
                        max_profits += stack[-1] - stack[0]
                    stack = [price]

                else:
                    stack.append(price)
        if len(stack) >= 2: return max_profits + stack[-1] - stack[0] # 尾部嚴格遞增
        return max_profits