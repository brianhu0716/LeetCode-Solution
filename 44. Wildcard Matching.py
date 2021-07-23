# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:17:33 2021

@author: Brian Hu
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(ps, pp):
            if (ps, pp) in self.dp:
                return self.dp[(ps, pp)]
            if ps == ls:
                for i in range(pp, lp):
                    if p[i].isalpha() or p[i] == '?':
                        return False
                return True
            if pp == lp:
                return True if ps == ls else False
            
            if p[pp] == '*': # match and continue to use * or match but won't use * or don't match * with char in s
                ans = helper(ps + 1, pp) | helper(ps + 1, pp + 1) | helper(ps, pp + 1)
            elif p[pp] == '?': # must match a char in s
                ans = helper(ps + 1, pp + 1)
            else:
                if p[pp] != s[ps]: # can't match, return False
                    ans = False
                else: # match and continue
                    ans = helper(ps + 1, pp + 1)
            self.dp[(ps, pp)] = ans
            return ans
        
        self.dp = dict()
        lp, ls = len(p), len(s)
        return helper(0, 0)