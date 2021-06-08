# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:19:46 2021

@author: Brian
"""
'''
幾A幾B遊戲：
(a) 比較兩者在相同位置的數字，如果一樣則A的數量+1，如果不一樣則留在字典中
(b)計算完A的數量後，我們把字典A中的key值拿出來遍歷，如果當前的key值在B中也有出現，則取兩字典中key對應的值較低者為B的個數，
    遍歷完成後結束
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        nA,nB = 0,0
        dictA,dictB = {},{}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                nA += 1
            else:
                dictA[secret[i]] = dictA.get(secret[i],0) + 1
                dictB[guess[i]] = dictB.get(guess[i],0) + 1
        for key in dictA.keys():
            if key in dictB.keys():
                nB += min(dictB[key],dictA[key])
        return str(nA) + "A" + str(nB) + "B"