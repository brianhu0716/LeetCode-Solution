# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 22:42:06 2021

@author: Brian
"""
'''
本題與1759一樣
'''
class Solution:
    def findLastWord(self,s,start,end,flag):
        for i in range(start, end):
            if s[i] != flag:
                return i
        return end
    def numSub(self, s: str) -> int:
        ls,i,ans = len(s),0,0
        while i < ls:
            if s[i] == "1":
                finish = self.findLastWord(s,i + 1,ls,s[i])
                ans += (1 + finish - i) * (finish - i) // 2
                i = finish
            else:
                i += 1
        return ans % 1000000007 if ans >= 1000000007 else ans