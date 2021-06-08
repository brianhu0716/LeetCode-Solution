# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:49:38 2021

@author: brian.hu
"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        table = dict()
        gap = list()
        for x in range(len(wall)) :
            cum_sum = 0
            gap.append(set())
            for y in range(len(wall[x]) - 1) : # 最後一個位置不能算(題目要求)
                cum_sum += wall[x][y]
                table[cum_sum] = table.get(cum_sum,0) + 1 # 存入gap位置出現在圖中的頻率
                gap[-1].add(cum_sum) # 存入每個row出現gap的位置
        if not table : return len(wall)
        
        # 找出出現頻率最高的gap位置
        width = cum_sum
        most_gap_postion,most_freq = float('-inf'),float('-inf')
        for gap_position,freq in table.items() :
            if freq > most_freq :
                most_freq = freq
                most_gap_postion = gap_position
        # 如果該gap沒有出現在當前row中，表示劃線時會被切到
        ans = 0
        for row in gap :
            if most_gap_postion not in row :
                ans += 1
        return ans