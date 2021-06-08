# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:00:35 2021

@author: Brian
"""

class Solution:
    def longestDecomposition(self, text: str) -> int:
        ptr = 1
        ans = 0
        while ptr < len(text):
            if text[:ptr] == text[len(text) - ptr :]:
                ans += 2
                text = text[ptr : len(text) - ptr ]
                ptr = 1
            else:
                ptr += 1
        
        return ans + 1 if text else ans