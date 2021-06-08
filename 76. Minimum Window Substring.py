# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:31:49 2021

@author: Brian
"""
class Solution:
    def notmissing(self,d1,d2):
        for key in d1.keys():
            if d1[key] < d2[key]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        ans = []
        d = {}
        for tt in t:
            if tt not in d.keys():
                d[tt] = 1
            else:
                d[tt] += 1
        lp = 0
        rp = float("-inf")
        d_now = {tt : 0 for tt in t}

        while True :
            rp_fixed = True
            for i in range(max(-1,rp) + 1,len(s)):
                if s[i] in d_now.keys():
                    d_now[s[i]] += 1
                    if self.notmissing(d_now,d):
                        rp_fixed = False
                        rp = i
                        break
            if rp == float('-inf'):
                return ""


            for i in range(lp,rp + 1):
                if s[i] in d_now.keys() and d_now[s[i]] - 1 >= d[s[i]]:
                    d_now[s[i]] -= 1
                elif s[i] in d_now.keys() and d_now[s[i]] - 1 < d[s[i]]:
                    lp = i
                    break

            if rp_fixed :
                break
            else:
                ans += [s[lp:rp + 1]]
                d_now[s[lp]] -= 1
                lp += 1

        return "" if not ans else ans[(l := [len(ss) for ss in ans]).index(min(l))]