# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:03:35 2021

@author: Brian
"""
'''
本題要找出兩字串之間是否存在能夠置換任一字串內部的兩個位置值使兩字串相等，分三種情況討論
(a) 如果兩字串長度不等，一定是false
(b) 如果我們發現相等的字串中出現超過兩個不同的位置，一定是false(代表至少要換三次)
    (b.1) 如果最後勝只有兩個字的位置不等，檢查是否交換後即可使兩字串相等，可以就是true，不行就是false
    (b.2) 如果發現所有字元都相等，檢查字典中各字元出現的頻率，只要有任一字元出現兩次以上一定是true否則是false
          因為如果都出現一次代表置換任兩位置的值都會造成兩字串不等
'''
class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        i_diff = []
        word_dict = {}
        for i in range(len(a)):
            if a[i] != b[i]:
                i_diff += [i]
                if len(i_diff) > 2:
                    return False
            else:
                word_dict[a[i]] = word_dict.get(a[i],0) + 1

        if len(i_diff) == 2 and a[i_diff[0]] == b[i_diff[1]] and a[i_diff[1]] == b[i_diff[0]]:
            return True
        elif len(i_diff) == 0:
            for i in word_dict.values():
                if i >= 2:
                    return True
            return False
        else:
            return False