# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 21:02:54 2021

@author: Brian
"""
'''
本題與第84題類似，我們建立一個遞增stack，如果當前的氣溫值比stack頂部位置對應的氣溫值大，則開始更新計算
之前氣溫低的日子到今天(ind)為止的天數(ind - day)，作法依樣為依次pop()出頂部的日子，值到stack頂部的位置
對應的氣溫比目前氣溫高後，將目前的日子放入stack頂部，繼續往下遍歷，直到找到比stack頂部氣溫高的日子在
更新值前的預測日期
'''
class Solution:
    def dailyTemperatures(self, T) :
        stack = list()
        pred = [0 for i in T] # 找不到就是0，因此我們初始化時設定為0較方便
        for ind,val in enumerate(T):
            if ind == 0: # 初始化stack
                stack.append(ind)
            if val <= T[stack[-1]]:
                stack.append(ind)
            else:
                while stack and T[stack[-1]] < val:
                    # day = stack.pop()
                    pred[prev_day] = ind - (prev_day := stack.pop())
                stack.append(ind)
        return pred
test = Solution()
T = [[73, 74, 75, 71, 69, 72, 76, 73]]
for i in T :
    print(test.dailyTemperatures(i))