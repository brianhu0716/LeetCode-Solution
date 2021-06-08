#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 07:18:22 2021

@author: brian
"""

class Solution:
    def customSortString(self, order: str, string: str) -> str:
        d = dict()
        rest = ""
        for char in string:
            if char in order :
                d[char] = d.get(char,0) + 1
            else :
                rest += char
            
        ans = ""
        for char in order :
            if char in d : # pass the char only appear in order
                ans += char * d[char]
        return ans + rest # add the string which appear only in string