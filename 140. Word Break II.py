# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:43:14 2021

@author: Brian
"""

class Solution:
    def wordBreak(self, s, wordDict):
        table = [[] for i in range(len(s) + 1)] # 第i個位置內含在第i個位置之前可以到第i個位置的所有組合
        for i in range(len(s)):
            # i = 0時需要初始化，若i != 0且table[i]是空的代表之前沒有任何組合可以走到第i個位置，continue
            if i != 0 and not table[i] : continue 
            for word in wordDict:
                if s[i : i + (lw := len(word))] == word:
                    if table[i]:
                        # table[i]有字代表之前已經有word可以走到table[i]，因此我們要基於之前的成果再加上當前的字走到table[i + lw]
                        table[i + lw] += [prefix + " " + word for prefix in table[i]] 
                    else:
                        table[i + lw] += [word] # 第一個word可以走到第i個位置(用該word當開頭)
                    print("title now :",s[i])
                    print("word now :" ,word)
                    print("table now :",table)
                    print("\n")
        return table[-1]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
test = Solution()
test.wordBreak(s,wordDict)
"""
title now : c
word now : cats
table now : [[], [], [], [], ['cats'], [], [], [], [], []]


title now : c
word now : cat
table now : [[], [], [], ['cat'], ['cats'], [], [], [], [], []]


title now : s
word now : sand
table now : [[], [], [], ['cat'], ['cats'], [], [], ['cat sand'], [], []]


title now : a
word now : and
table now : [[], [], [], ['cat'], ['cats'], [], [], ['cat sand', 'cats and'], [], []]
"""