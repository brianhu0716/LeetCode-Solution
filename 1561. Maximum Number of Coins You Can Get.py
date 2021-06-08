# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:12:39 2021

@author: brian.hu
"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        p1,p2 = 0,len(piles) - 1
        ans = 0
        while p1 < p2 :
            ans += piles[p2 - 1]
            p2 -= 2
            p1 += 1
        return ans