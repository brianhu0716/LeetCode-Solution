# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:22:50 2021

@author: Brian
"""
'''
一串有效表示地括號混合數字中，要計算被括號包到最多次的數字的括號次數。解題思路如下：
如果遇到"("就直接加1，這代表右方的數字被一組括號包住，同時更新到目前為止遇到被最多括號包住的括號數，
遇到")"減1，代表接下來的數字少一組括號包覆；遍歷一次即可得到答案

'''

class Solution:
    def maxDepth(self, s: str) -> int:
        max_p = 0
        now_p = 0
        for ss in s:
            if ss == "(" :
                now_p += 1
                max_p = max(max_p,now_p)
            elif ss == ")":
                now_p -= 1
            else:
                continue
        return max_p