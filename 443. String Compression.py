# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:56:41 2021

@author: Brian
"""
'''
本題目標是希望將chars中重複出現(次數大於2)的字母以字母+次數的形式進行壓縮(ex:["a","a","a"] - > ["a","3"])
而只連續出現一次的字母不動。解題思路如下:
(a) 定義一個找出與起始點不同的第一個字母的函數(findFirstFalseElement)，利用該函數找到下一個起始位置
(b) 直接將該位置減去起始位置即為起始字母連續且重複出現的次數，將該次數轉成字元後取代重複出現的字母，
    並將多餘位置移除，最後更新起始點直到末端即可
*** 如果chars的末端也是連續出現的字母的一部分時，我們直接把下一個不等於起始字母的位置設成len(chars)，
    如此即可不影響主程式中計算重複次數的邏輯
'''
class Solution:
    def findFirstFalseElement(self,start,chars):
        for i in range(start,l := len(chars)):
            if chars[i] != chars[start]:
                return i
        if i == l - 1: # 如果末端是連續出現的字母的一部分時，我們直接把下一個不等於起始字母的位置設成len(chars)
            return l
    def compress(self, chars):
        start = 0
        while start < len(chars):
            i = self.findFirstFalseElement(start,chars)
            if (n := i - start) >= 2:
                r = []
                while n != 0:
                    r += [str(n % 10)]
                    n = n // 10
                chars[start + 1:(end := start + 1 + len(r))] = r[::-1]
                del chars[end:i]
                start = end
            else:
                start = i
        print(chars)
test = Solution()
chars = [["a","a","b","b","c","c","c"],
         ["a"],
         ["a","b","b","b","b","b","b","b","b","b","b","b","b"],
         ["a","a","a","b","b","a","a"],
         ["p","p","p","p","m","m","b","b","b","b","b","u","u","r","r","u","n","n","n","n","n","n","n","n","n","n","n","u","u","u","u","a","a","u","u","r","r","r","s","s","a","a","y","y","y","g","g","g","g","g"]]

for s in chars:
    test.compress(s)
