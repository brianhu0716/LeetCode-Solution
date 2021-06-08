# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:17:42 2021

@author: Brian
"""
'''
計算切蛋糕的最大面積，方法為計算每一刀之間的間距，分別找出橫切與縱切的最寬距離後相乘即為答案
*** 提前終止條件為當目前最大間距比遍界到當前的位置還要大時，可以提前終止，因為最想的情況(邊界到當前距離一刀
   也無法比當前最大間距大)

'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        maxh,maxw = float('-inf'),float('-inf')
        for i in range(1,len(horizontalCuts)):
            maxh = max(maxh,horizontalCuts[i] - horizontalCuts[i - 1])
            if maxh >= horizontalCuts[-1] - horizontalCuts[i]:
                break
        for i in range(1,len(verticalCuts)):
            maxw = max(maxw,verticalCuts[i] - verticalCuts[i - 1])
            if maxw >= verticalCuts[-1] - verticalCuts[i]:
                break
                
        return maxh * maxw if maxh * maxw < 1000000007 else maxh * maxw % 1000000007