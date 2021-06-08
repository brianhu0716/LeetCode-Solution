# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:10:52 2021

@author: brian.hu
"""
"""
創造出最短的palindrome(只能在原本字串的前方加字)
作法：
利用右指標j由右往左搜索，如果s[ : j]是palindrome，則我們只需要將s[j : ][::-1]加到s的前方
即可形成回文

"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        j = len(s) 
        while j >= 0 :
            if s[ : j] == s[ : j][::-1] :
                break
            j -= 1
        return s[j : ][::-1] + s