# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:27:03 2021

@author: Brian
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ss in s:
            if ss not in d.keys():
                d[ss] = 1
            else:
                d[ss] += 1
        table = sorted([[d[key],key] for key in d.keys()])
        ans = ''
        for i in range(len(table) - 1,-1,-1):
            ans += table[i][1] * table[i][0]
        return ans