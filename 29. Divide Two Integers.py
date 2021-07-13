# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:15:36 2021

@author: Brian Hu
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = int(dividend / divisor)
        return min(2 ** 31 - 1, n) if n >= 0 else max(-2 ** 31, n) 