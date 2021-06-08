# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:24:16 2021

@author: Brian
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d,repeat = dict(),list()
        for n in nums:
            d[n] = d.get(n,0) + 1
            if d[n] == 2: repeat.append(n)
        return repeat