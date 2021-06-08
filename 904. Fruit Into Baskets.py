# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:31:25 2021

@author: Brian
"""
'''
本題要求在兩個籃子個只能裝一種水果的前提下，如何拿才能得到最多的水果，基本流程如下
只要藍還有空的我們就把當前不同品種的水果裝到剩的籃子中(兩個藍分別以stack1以及stack2表示)，且stack中裝的是index，並將當前裝的
兩種品種存放到fruit中，接著只要發現當前的水果品種與fruit中的不同，則把兩籃子頂端最靠近當前index的水果保留下來，另一藍清空
並繼續累加當前兩種水果的出現次數。
*** 值得注意的是，由於兩籃中的水果的index可能是交錯出現，一但選定要刪除的一籃水果後，在這籃水果最頂端的index之前的所有欲保存
的水果(另一籃)的index全部都要跟著被移除，完成後再total中新增一個element統計現在這兩種水果的連續出現次數
'''
class Solution:
    def totalFruit(self, tree) -> int:
        def findFirstless(stack,ref): 找到欲保存下來的水果的邊界
            for i in range(len(stack) - 1,-1,-1):
                if stack[i] < ref:
                    return i
            return -1
        fruit,stack1,stack2,total = [],[],[],[0]
        for idx,val in enumerate(tree):
            if val in fruit:
                stack1.append(idx) if val == fruit[0] else stack2.append(idx)
                total[-1] += 1
            else:
                if not stack1 or not stack2: # 還有空籃子，優先將兩籃各裝一種水果
                    fruit.insert(0,val) if not stack1 else fruit.append(val)
                    stack1.append(idx) if not stack1 else stack2.append(idx)
                    total[-1] += 1
                else:
                    if stack1[-1] > stack2[-1] :
                        stack1 = stack1[findFirstless(stack1,stack2[-1]) + 1:]
                        stack2 = [idx]
                        fruit[1] = val
                    else:
                        stack2 = stack2[findFirstless(stack2,stack1[-1]) + 1:]
                        stack1 = [idx]
                        fruit[0] = val
                    total.append(len(stack1) + len(stack2)) # 初始化新的統計
        return max(total)