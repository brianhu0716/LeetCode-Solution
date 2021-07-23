# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:05:35 2021

@author: Brian Hu
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(ps, pp, p, s):
            if (ps, pp) in self.dp:
                return self.dp[(ps, pp)]
            if ps == ls:
                for i in range(pp, lp):
                    if p[i].isalpha() or p[i] == '.':
                        if i + 1 < lp and p[i + 1] == '*':
                            continue
                        return False
                return True
            if pp == lp:
                return False if ps != ls else True
            
            if p[pp] == '*': 
                if p[pp - 1].isalpha() and p[pp - 1] != s[ps]: # * can only represent the previous char, since char != targrt, we can only push pp forward to match s[ps]
                    ans = helper(ps, pp + 1, p, s)
                else: # * can represent the previous char and continue to use it or move forward. Or * can't represent the current char
                    ans = helper(ps + 1, pp, p, s) | helper(ps + 1, pp + 1, p, s) | \
                            helper(ps, pp + 1, p, s) 
            elif p[pp] == '.':
                if pp + 1 != lp and p[pp + 1] == '*': # leave it to * case to deal it with
                    ans = helper(ps, pp + 1, p, s)
                else: # if non * after ., it must to match a char in s
                    ans = helper(ps + 1, pp + 1, p, s)
            else:
                if p[pp] == s[ps]:
                    if (pp + 1 != lp and p[pp + 1] != '*') or (pp + 1 == lp): # must to match a char in s
                        ans = helper(ps + 1, pp + 1, p, s)
                    else: # leave it to * to deal it with
                        ans = helper(ps, pp + 1, p, s)
                else: 
                    if (pp + 1 == lp) or (pp + 1 < lp and p[pp + 1] != '*'): # can't match, return False
                        ans = False
                    else: # means the char(p[pp]) repeat 0 times
                        ans = helper(ps, pp + 2, p, s)
                
            self.dp[(ps, pp)] = ans
            return ans
        
        self.dp = dict()
        ls, lp = len(s), len(p)
        return helper(0, 0, p, s)