# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:33:42 2021

@author: Brian
"""
class Solution:
    def findSubstring(self, s, words):
        words,ind = sorted(words),[]
        w_len = len(words[0])
        total_len = len(words) * w_len
        for i in range(0,len(s) - total_len + 1):
            window = s[i:i + total_len]
            res = []
            for j in range(0,total_len,w_len):
                res.append(window[j:j + w_len])
            if sorted(res) == words:
                ind += [i]
        return ind