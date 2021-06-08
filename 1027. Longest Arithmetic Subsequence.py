# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:24:23 2021

@author: Brian
"""
'''
本題要求找出list A中最長的等差數列長度，解題思路如下：
(a) 初始化一個長度與A相同的table，個元素均為空字典，個位置的字典在未來要放入到該位置之前(含該位置)各公差的出現的總數
(b) 外部迴圈控制當前位置，內部迴圈控制該位置之前的值，內部迴圈每向前一個位置，我們就計算該位置值(A[j])與外部迴圈選定的位置值(A[i])
    的差，如果diff已經出現在table[i]的key中，則跳過(代表A[j]是一個重複出現的值)；若沒有則進行以下判斷
    (b.1)若這個差(diff)已經出現在table[j]的key中，代表該公差在位置j之前已經出現過，此時我們將table[i]中加入該diff作為鍵，其對應的
        值應為table[j][diff] + 1(代表加入自己(A[i])後的長度)。
    (b.2)如果diff沒有出現在table[j]的key中，則將table[i]中加入diff為鍵，對應的值定為2，代表自己(A[i])與A[j]兩個元素的長度
***** 特別要注意的是：內部迴圈遍歷的順序應由後往前，因為如果[0,i]之間有重複出現的數字，我們累積的等差數列最大長度會出現在
        最靠近i的數字的字典中，因此我們必須要由後往前檢視，避免計算到較短的長度導致之後較長的長度被忽略(看test case)
***** 如果堅持要由前往後遍歷，遇到已經出在table[i]的key值的diff，不可以跳過，必須要先對該key對應的值做更新
        (因為這時候已經存在table[i][diff]的值會比較小，要把他替換成較長的值)
        --> table[i][diff] = max(table[i][diff],table[j][diff] + 1 if diff in table[j].keys() else 2)
'''
# j由i - 1 -- > 0遍歷
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        table = [{} for _ in A]
        for i in range(len(A)):
            for j in range(i - 1,-1,-1):
                if (diff := A[i] - A[j]) not in table[i].keys():
                    if diff in table[j].keys():
                        table[i][diff] = table[j][diff] + 1
                    else:
                        table[i][diff] = 2
        return max([max(sub_table.values()) for sub_table in table if sub_table])


test_case = [6,4,5,12,5,6,7]

### j由0 -- > i - 1遍歷
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        table = [{} for _ in A]
        for i in range(0,len(A)):
            for j in range(0,i):
                if (diff := A[i] - A[j]) not in table[i].keys():
                    if diff in table[j].keys():
                        table[i][diff] = table[j][diff] + 1 
                    else :
                        table[i][diff] = 2
                else:
                    table[i][diff] = max(table[i][diff],table[j][diff] + 1 if diff in table[j].keys() else 2) # *****
                

        return max([max(sub_table.values()) for sub_table in table if sub_table])
