# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:39:52 2021

@author: brian.hu
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        result = ""
        for i in range(len(s) - 1,-1,-1) :
            char = s[i]
            if char == " " :
                if not word : continue # 字與字之間有多餘的空白，忽略
                result += word + " "
                word = ""
            else :
                word = char + word 
        # 第一個字之後如果有空白，會在loop中被更新，但尾部會多出一個" "需要移除，
        # 否則讀到的word必須加到result中
        return result + word if s[0] != " " else result[: -1] 