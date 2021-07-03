# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:54:13 2021

@author: Brian Hu
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l, n = len(part), len(s)
        ans = ''
        for i in range(n):
            ans += s[i]
            if ans[-1] == part[-1]: # part might in the tail of ans
                if (start := len(ans) - l) >= 0 and ans[start: ] == part:
                    ans = ans[: start]
        return ans