# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:55:07 2021

@author: Brian
"""
"""
字串中有數字有英文字母，若遇到字母可以產生大小寫兩種不同組合，求所有的組合
(a) 初始化ans，如果字串中第一個字是數字，則把該數字放入ans，若是英文字母則將他的大小寫分別放入ans
(b) 按照同樣的邏輯，在遍歷過程中只要是數字就加入之前各組合的尾部。若遇到英文字就分別將她的小寫加入之前各組合的尾部；
    再將他的大寫加入之前各組合的尾部，再將兩個list連接即為當前所有可能的組合
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        (ans := [S[0]]) if S[0].isnumeric() else (ans := [S[0].lower(),S[0].upper()]) 
        for i in range(1,len(S)):
            if S[i].isnumeric():
                ans = list(map(lambda x : x + S[i], ans))
            else :
                res = ans[:]
                ans = list(map(lambda x : x + S[i].lower(),res)) +  list(map(lambda x : x + S[i].upper(),res))
        return ans