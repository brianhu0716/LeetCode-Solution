# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:58:49 2021

@author: Brian Hu
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, l = len(strs[0]), len(strs)
        valid_col_idx, rmv = list(), 0
        for i in range(n):
            valid_col = True
            for j in range(1,l): # check whether this col is non-decreasing or not 
                if strs[j][i] < strs[j - 1][i]:
                    if not valid_col_idx: # no previous valid col can compensate
                        valid_col = False
                        break
                    pass_this = False
                    for col in valid_col_idx[::-1]:
                        if strs[j][col] > strs[j - 1][col]: # exists previous col is non-drcreasing
                            pass_this = True 
                            break
                    if not pass_this: # early stop, because this col violates the condition
                        valid_col = False
                        break
                            
            if valid_col:
                valid_col_idx.append(i) # add a new valid col index
            else:
                rmv += 1 # remove this col
                    
        return rmv
                    