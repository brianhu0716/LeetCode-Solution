# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:36:58 2021

@author: Brian
"""
'''
建立一個字典累積各數字出現的次數，等到pop時找到出現頻率最高的次數由後往前找，找到第一個出現該次數的數字pop即可
'''
class FreqStack:

    def __init__(self):
        self.stack = list()
        self.freq = dict()
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.freq.get(val,0) + 1
    def pop(self) -> int:
        max_freq = max(self.freq.values())
        for i in range(len(self.stack) - 1,-1,-1):
            if self.freq[self.stack[i]] == max_freq:
                self.freq[self.stack[i]] -= 1
                return self.stack.pop(i)