# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:17:27 2021

@author: Brian
"""
'''
本題重點：只有六個值(骰子就6個面)。同一個數字要取個數多的作分析，因為要盡量交換較少的次數。第三：如果同一個位置出現相同的數字，
            只能算一次，因為交換後還是一樣的結果
(a) 先設兩個字典將骰子值對應的位置各自儲存至字典中
(b) 接著用一個list內包含6個set來記錄每個每個骰子值出現的總次數，遍歷完數據後我們可以以該list中各set的長度得知當前的數字是否有可能
    完全被A或B交換順序後獲得(如果set中的長度小於總長l，代表該數字根本不足，無論拿A補B或拿B補A都不可能使A或B交換後完全變該數字)
(c) 如果某數字的長度等於l，階者我們需要透過字典檢驗出現該數字較少的序列中，出現該數字的index是否與A有重複，只要有重複總數就必須減1
    這代表該位置上A以及B都是同樣的數字，不需要交換，最後把較少出現該數字的序列中該數字出現的總數減完同一位置共同出現的數字總數後，
    得到的答案先存入ans中，最後找小值即可
        

'''
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        dA = {i : list() for i in range(1,7)}
        dB = {i : list() for i in range(1,7)}
        total_len = [set() for i in range(1,7)]
        same = [0 for i in range(1,7)]
        for i in range(l := len(A)):
            dA[A[i]].append(i)
            dB[B[i]].append(i)
            total_len[A[i] - 1].add(i)
            total_len[B[i] - 1].add(i)
            if A[i] == B[i] : same[A[i] - 1] += 1
                
        ans = list()        
        for n in range(1,7):
            if len(total_len[n - 1]) != l: continue
            ans.append(len(dB[n]) - same[n - 1]) if len(dA[n]) >= len(dB[n]) else ans.append(len(dA[n]) - same[n - 1])

        return min(ans) if ans else -1