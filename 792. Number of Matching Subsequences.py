# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:01:47 2021

@author: Brian
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def checkSubset(s,word,d):
            lp = 0
            for rp in range(len(word)):
                if word[rp] not in d.keys(): return False # word出現s中不存在的字
                idx = s.find(word[rp],lp) # 順序不可以被打亂，所以s的起點必定是第一個找到等於word[rp]的位置
                if idx == -1: return False # s中找不到word中的字
                lp = idx + 1
            return True
        ans = 0
        d,l = dict(),len(s)
        for ss in s: d[ss] = d.get(ss,0) + 1
            
        for word in words:
            if checkSubset(s,word,d): ans += 1
        return ans
                    