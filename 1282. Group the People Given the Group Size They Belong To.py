# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:05:47 2021

@author: Brian
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        table = dict()
        for peopleIdx,groupSize in enumerate(groupSizes):
            if groupSize not in table.keys():
                table[groupSize] = [peopleIdx]
            else:
                table[groupSize].append(peopleIdx)
        ans = []
        for groupSize in table.keys():
            if len(table[groupSize]) == groupSize: # 人數剛好與groupSize相當
                ans += [table[groupSize]]
            else:
                for i in range(0,len(table[groupSize]),groupSize): # 人數為groupSize的整數倍時，按groupSize分組
                    ans += [table[groupSize][i : i + groupSize]]
        return ans