# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:53:10 2021

@author: Brian
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        lb,rb = [],[]
        for idx,char in enumerate(S):
            if char == "(":
                lb.append(idx)
            else:
                if lb and idx > lb[-1]: # 右括號的位置必須在左括號的右方才可以配成一組
                    lb.pop()
                else: # 若否，代表該右括號缺一個左括號配對
                    rb.append(idx)
        return len(lb) + len(rb)