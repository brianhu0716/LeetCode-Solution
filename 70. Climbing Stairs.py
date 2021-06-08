# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:38:21 2021

@author: Brian
"""
'''
爬樓梯問題：每次可以走1或2步，問走n步有幾種走法，我們列舉關係式如下
n = 1 --> 1種走法
n = 2 -- > 2種走法([1,1],[2])
n = 3 -- > 3種走法([1,1,1],[1,2],[2,1])
n = 4 -- > 5種走法([1,1,1,1],[2,2],[1,2,1],[2,1,1],[1,1,2])
由上面的列舉可以看出f(n) = f(n - 1) + f(n - 2)的遞迴式，也就是說我們要知道走n步有幾種走法，必須先知道走n - 1步以及走n - 2步有幾
種走法，因此我們利用遞迴可以解這樣的問題

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n in self.d.keys(): return self.d[n]
            if n <= 1: return 1
            self.d[n] = fib(n - 1) + fib(n - 2)
            return self.d[n]
        self.d = {}
        return fib(n)