# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:30:04 2021

@author: Brian
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd,even = list(),list()
        for n in A:
            if n % 2 == 1: odd.append(n)
            else: even.append(n)
        return even + odd