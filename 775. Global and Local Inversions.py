# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 22:11:48 2021

@author: Brian
"""
'''
關鍵：如果是global inversion,就一定是local inversion，但local inversion只存在於下一個位置的值比它大而已，位置差
超過1，就算global inversion了，因此我們用一個stack來記錄nums中比當前位置還要大的index，待遇到比stack[-1]的位置值小
的時候進行分析(由於我們已經知道位置差只要超過1，global的數量就會超越local，因此stack中只要保存與當前位置最近的兩個
局部極大值即可)
(a) 一旦當前值比之前的極大值小，且當前的位置值與最近的極大值位置差超過1，即return False，否則再判斷倒數第二近的極大值
    如果發現該值比當前值小，則程式繼續運作(ex:[3,7,6]-->stack[0,1],val = 6,ind = 2)，直到找到反例為止，如果遍歷序列
    後步出現這種情況，則return True
'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        stack = []
        nlocal,nglobal = 0,0
        for ind,val in enumerate(A):
            if not stack :
                stack.append(ind)
            elif val > A[stack[-1]] :
                stack.append(ind)
                if len(stack) == 3:
                    stack.pop(0)
            else:
                for idx_prev in stack[::-1]:
                    if A[idx_prev] > val :
                        nglobal += 1
                        if ind - idx_prev == 1:
                            nlocal += 1

                        if nglobal > nlocal:
                            return False
                    else:
                        break
        return True
    '''最精簡版
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        stack = []
        for ind,val in enumerate(A):
            if not stack :
                stack.append(ind)
            elif val > A[stack[-1]] :
                stack.append(ind)
                stack.pop(0) if len(stack) == 3 else stack                   
            else:
                for idx_prev in stack[::-1]:
                    if A[idx_prev] > val :
                        if ind - idx_prev > 1:
                            return False
                    else:
                        break
        return True
    '''