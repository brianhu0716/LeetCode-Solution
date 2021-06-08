# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:51:57 2021

@author: Brian
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {"U" : 0 , "D" : 0, "R" : 0 , "L" : 0}
        for move in moves:
            d[move] += 1
            
        return True if d["U"] == d["D"] and d["R"] == d["L"] else False