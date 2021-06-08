# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:50:20 2021

@author: Brian
"""

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = list()
        arr = [i for i in range(1,m + 1)]
        for n in queries:
            idx = arr.index(n)
            ans.append(idx)
            arr.insert(0,arr.pop(idx))
        return ans