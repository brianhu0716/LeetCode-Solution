# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:11:18 2021

@author: Brian
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        value = [1,5,10,50,100,500,1000]
        symbol = ['I','V','X','L','C','D','M']
        index = [0 for i in range(len(s))]
        for i in range(len(s)):
            for j in range(len(symbol)):
                if s[i] == symbol[j]:
                    index[i] = j
            
        result = 0
        i = 0
        while True: 
            if i == len(index) - 1:
                result += value[index[i]]
                i += 1
            elif i > len(index) - 1:
                break
            else:
                if index[i] < index[i + 1]:
                    result += value[index[i + 1]] - value[index[i]]
                    i += 2
                else:
                    result += value[index[i]]
                    i += 1
            
            
        return result