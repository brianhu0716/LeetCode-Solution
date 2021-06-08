# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:16:37 2021

@author: Brian
"""

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = []
        threshold = float('-inf')
        for word in dictionary:
            if (lw := len(word)) < threshold: continue # 當前word的長度比已知答案中的word的長度短，跳過(因為最後要取長度較長的)
            start = 0 # 搜索s的起始位置
            for rp in range(lw):
                idx = s.find(word[rp],start)
                if idx == -1 : break
                start = idx + 1
            if idx == -1: # s中沒有與word[rp]匹配的字，代表該word不能透過刪除特定s中的字來獲得，所以當前的word不是答案
                continue
            else:
                if not ans:
                    ans.append(word) 
                else: 
                    (ans := [word]) if lw > len(ans[-1]) else ans.append(word) # 如果當前符合資個的word長度比已知答案的word長，以當前的word長度為新的門檻值
                threshold = len(ans[-1]) 
        return sorted(ans)[0] if ans else "" # 最終答案已經確保所有的word長度都一樣，只需要取開頭字母最小的回傳即可