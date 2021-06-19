# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 00:51:50 2021

@author: Brian
"""

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0: return []
        bx = int(log(bound) / log(x)) if x > 1 else 0 
        by = int(log(bound) / log(y)) if y > 1 else 0
        ans = set()
        for i in range(bx + 1):
            for j in range(by + 1):
                if (tot := x ** i + y ** j) <= bound:
                    ans.add(tot)
        return ans
