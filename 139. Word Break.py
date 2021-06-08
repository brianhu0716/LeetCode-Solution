# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:50:33 2021

@author: Brian
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False for i in range(len(s) + 1)]
        for i in range(len(s)):
            if i != 0 and table[i] == False: continue # i = 0時需要初始化，i != 0且table[i]又是空的代表之前沒有字可以走到table[i]，則直接continue

            for word in wordDict:
                if s[i : i + (lw := len(word))] == word:
                    table[i + lw] = True # 把可以到達的位置更新

            
            if table[-1] == True: return True # 終點已經是True可以提前終止
        return False