# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:15:28 2021

@author: Brian
"""
'''
動態規劃：我們想要知道走到座標(m - 1,n - 1)有多少種可能時，我們必須先知道走到座標(m - 2,n - 1)以及座標(m - 1,n - 2)有多少種可能
並把結果相加(因為我們只能往右或往下走)。由此可以列出地回關係式：f(m - 1,n - 1) = f(m - 2,n - 1) + f(m - 1,n - 2)
***邊界條件：因為我們只能往右或往下走，因此當座標在邊界時(row = 0 or col = 0)，只會有一種走法，不是一路往右就是一路往下(一種走法)，
故邊界條件回傳1
*** memorization:每計算一次走到該座標有幾種可能時，就先記錄起來(存在字典)，等到之後需要用可以提取
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.d = {}
        def countPath(row,col):
            if (row,col) in self.d.keys(): return self.d[(row,col)]
            if row == 0 or col == 0: return 1

            
            temp1 = countPath(row - 1,col)
            self.d[(row - 1,col)] = temp1
            temp2 = countPath(row,col - 1)
            self.d[(row,col - 1)] = temp2

            return temp1 + temp2 
            
        return countPath(m - 1,n - 1)