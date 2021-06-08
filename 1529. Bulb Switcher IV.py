# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:55:02 2021

@author: Brian
"""
'''
看到target中有1就翻一次，接者從1的位置開始找，直到target有0的位置在翻一次；接著再從0的位置開始找到第一個1...直到找到末尾為止
'''
class Solution:
    def minFlips(self, target: str) -> int:
        start0,n,l = 0,0,len(target)
        while True:
            for i in range(start0,l + 1):
                if i == l: return n
                if target[i] == "1":
                    start1 = i
                    break
            n += 1
            for j in range(start1,l + 1):
                if j == l: return n
                if target[j] == "0":
                    start0 = j
                    break
            n += 1