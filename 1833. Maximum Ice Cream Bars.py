# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:02:28 2021

@author: Brian
"""

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for cost in costs:
            if cost > coins: break
            coins -= cost # 要盡可能地買到最多的冰淇淋，必須從金額最少的開始買，值到手上的錢比當前金額的冰淇淋少為止
            ans += 1
        return ans