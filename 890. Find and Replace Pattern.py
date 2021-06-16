# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:57:22 2021

@author: Brian Hu
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        cnt, mode, transfer = 0, dict(), ""
        for char in pattern: # encrypt original string form char to number
            if char in mode:
                transfer += str(mode[char])
            else:
                mode[char] = cnt
                transfer += str(cnt)
                cnt += 1
        ans = list()
        for word in words:
            d, cnt, match = dict(), 0, True
            s = ""
            for j, char in enumerate(word): # encrypt word form char to number
                if char in d:
                    code = d[char]
                else:
                    d[char] = cnt
                    code = cnt
                    cnt += 1
                s += str(code)
            
            if s == transfer: # if encrypted word == encrypted pattern: find an answer
                ans.append(word)

            
        return ans