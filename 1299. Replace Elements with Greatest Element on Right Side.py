# -*- coding: utf-8 -*-
"""。
Created on Sat Apr 10 21:03:29 2021

@author: Brian
"""
'''
本題需要找到比當前index更大的最大值放入output對應的當前位置中，解題思路如下：
(a) 其實在第一次找最大值時我們已經看過所有資料了，因此與其每前進一個位置重新找最大值，不如我們先把序列值由小排到大，且每個值都包含
    其原本在序列的位置，之後我們只需要比對當前位置的i 是否有比table中最頂部的值的index小即可
    (a.1) 如果當前index小於table最頂部的index，則當前位置的最大值就是table最頂端的值
    (a.2) 如果發現當前的index大於或等於table最頂部的index(代表table頂端的最大值出現在當前位置之前)，必須要往下一個極大值找，透過
            不斷的pop直到當前index小於table最頂部的index為止。如果發現此時table已經空了，表示當前位置已經到最後一個位置，所以沒有人
            在右邊，此時只要補-1即可回傳
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        table = sorted([[val,idx] for idx,val in enumerate(arr)])
        output = list()
        for i in range(0,len(arr) - 1):
            if table[-1][1] > i:output.append(table[-1][0])
            else :#table[-1][1] <= i:
                while table and table[-1][1] <= i:
                    table.pop()
                if table : 
                    output.append(table[-1][0])
                else: 
                    output.append(-1)
                    return output
        output.append(-1)
        return output