# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:52:09 2021

@author: brian.hu
"""
"""
逆向思考，最後一個插入的"abc"一定是連續的，所以我們依序搜尋字串，字串只要出現連續的"abc"
就移除，並更新新的搜尋起點，逐漸移除連續的"abc"字串，直到中止條件為止
(a) 如果string沒有字：代表滿足題目要求，return True
(b) 如果leading character 是"b"或"c"，代表不可能由"abc"插入構成，又或著字傳剩餘長度小於3
    則return False
(c) 如果上一次字串的長度與更新後的長度一樣，代表無法再優化，return False
"""
class Solution:
    def isValid(self, s: str) -> bool:
        l_old = float('inf')
        while len(s) != l_old : # 無法再減少string的長度
            l_old = len(s)
            i = 0
            while i < len(s) :
                if s[i : i + 3] == "abc" :
                    s = s[ : i] + s[i + 3 : ]
                    i = i - 2 if i >= 2 else 0
                else :
                    i += 1
                    
                if not s : return True 
                elif s[0] == "b" or s[0] == "c" or len(s) < 3 : return False
                
        return False