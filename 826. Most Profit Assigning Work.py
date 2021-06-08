# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:50:59 2021

@author: Brian
"""
'''
本題需要找出每位工人的最大獲利情況，每位工人都有能力上限，不能做難度比它上限更高的工作，但由於獲利與難度不是成正比的，因此
我們將專案獲利與難度綁再一起，並根據難度做排序，接著也把工人的能力做排序，外圈loop每次更新時只考慮能力值界於當前難度與下一
個難度之間的工人，他們可以選擇執行的專案最大獲利為把當前難度的專案獲利與之前的最大獲利比較大小後取大值，一路更新到最後一位工人
即可得到答案
*** 考慮到有工人能力值可能比難度最低的專案更低，因此我們在難度-獲利表中的第一項增加(0,0)，代表能力值界於0 - 專案最低難度 的工人
他們的獲利是0(因為沒有專案可執行)。又考慮可能有工人能力大於最難的專案，因此在難度-獲利表中的最後一項增加(inf,max(profit))這一項
代表能力值大於最困難的專案的工人可以選擇的最大獲利為所有獲利中利潤最大的專案執行
'''
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs = sorted(zip(difficulty,profit))
        pairs = [(0,0)] + pairs + [(float('inf'),pairs[-1][1])]
        worker.sort()
        rp,max_profit_now,ans = 0,0,0                                   
        for i in range(len(pairs) - 1):
            up,down,max_profit_now = pairs[i + 1][0],pairs[i][0],max(max_profit_now,pairs[i][1])
            for j in range(rp,len(worker)):                     
                if up > worker[j] >= down :
                    ans += max_profit_now
                else:
                    rp = j
                    break
        return ans
difficulty = [68,35,52,47,86]
profit = [67,17,1,81,3]
worker = [92,10,85,84,82]