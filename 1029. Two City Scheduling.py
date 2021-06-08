# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:17:39 2021

@author: Brian
"""
'''
本題給出每人到兩個城市所需要花費的成本，需要找出讓所有的人都以最低的成本到達其中一個城市，且兩城市中的人數必須要一樣多
解題思路如下：
(a) 我們只要算出每個人的第一個城市到第二個城市的差後由小到大排序，差值越小的代表到第二個城市比到第一個城市的成本大最多，因此這個
    人一定要被分到去第一個城市，依此類推，當第一的城市的人數累積到一半時，剩下的人就必須到第二個城市去，如此一來成本一定會最低
*** diff除了紀錄到兩城市間的成本差值外，還記錄了該人的編號方便我們後續排序後可以快找到原始人員位置
'''

ans = 0
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff,ans,l = list(),0,len(costs)
        for i in range(l):
            diff.append([costs[i][0] - costs[i][1],i]) # 
        diff = sorted(diff)
        for i in range(l):
            idx = diff[i][1]
            (ans := ans + costs[idx][0]) if i < l // 2 else (ans := ans + costs[idx][1])
        return ans
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]