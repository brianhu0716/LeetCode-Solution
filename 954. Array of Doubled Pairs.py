#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:37:12 2021

@author: brian
"""
"""
if num < 0 : eliminate the exist number with value is twice times as it ,
if num >= 0 : eliminate the exist number with value is one-half as than it
"""
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        table = dict()
        for n in arr :
            if n >= 0 and (x := n // 2) * 2 == n and x in table :
                table[x] -= 1 
                if table[x] == 0 : del table[x]
            elif n < 0 and 2 * n in table :
                table[2 * n] -= 1 
                if table[2 * n] == 0 : del table[2 * n]
            else :
                table[n] = table.get(n,0) + 1
            #print(table)
        #print(table)
        if table : return False
        return True