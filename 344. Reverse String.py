# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:19:52 2021

@author: Brian
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lp,rp = 0,len(s) - 1
        while lp < rp:
            s[lp],s[rp] = s[rp],s[lp]
            rp -= 1
            lp += 1