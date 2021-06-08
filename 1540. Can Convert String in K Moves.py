# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:07:02 2021

@author: Brian
"""

import string
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        d = {string.ascii_lowercase[i] : i + 1 for i in range(26)}
        move_used = dict()
        for idx,char in enumerate(s):
            
            if char != t[idx]:
                if d[t[idx]] > d[char]: 
                    move = d[t[idx]] - d[char]
                else:
                    move = d[t[idx]] - d[char] + 26 # wrap(ex: y -- > b)

                if move not in move_used.keys(): # 只有1~25這幾種間隔的整數倍
                    move_used[move] = [move]
                else: # 如果算出來的間隔已經存在，就再多繞一圈(+26)
                    move_used[move].append(move_used[move][-1] + 26)
            else : continue
                
            if move_used[move][-1] > k: return False # 如果所需要的步數超出限制(k)，False
                
        return True