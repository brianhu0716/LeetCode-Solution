# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:18:45 2021

@author: Brian
"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def CountSoliders(row):
            for i in range(l := len(row)):
                if row[i] == 0:
                    return i
            return l
        
        sr = [] # soliders of each row
        for i in range(len(mat)):
            sr.append([CountSoliders(mat[i]),i])
        return [r[1] for r in sorted(sr)[:k]]