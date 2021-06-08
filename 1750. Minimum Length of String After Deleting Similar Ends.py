# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:03:56 2021

@author: Brian
"""
'''
本題目標為搜尋一個字串中，第一次出現頭尾不同時的長度為何
作法為
(a) 先檢查頭尾是否相同，如果相同，則由頭開始找出第一個不與字首相同的位置，同樣的由尾開始搜索找出第一個不與字首相同
    的位置；接著重複(a)直到第一次出現首尾不同，即終止程式
*** 如果剩下一個字元，則不執行判斷，return 1

'''
def findSameChar(s,reversed = False):
    (s := s[::-1]) if reversed else s
    for i in range(1,ls := len(s)):
        if s[i] != s[0]:
            return i
    if i == ls - 1:
        return ls

s = "aabccabba"
s = "cabaabac"
# s = "ca"
s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
while len(s) > 1:
    if s[0] == s[-1]:
        s = s[findSameChar(s,reversed = False):len(s) - findSameChar(s,reversed = True)]
        print(s)
    else:
        break
print(len(s))
    