# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:28:30 2021

@author: Brian
"""
'''
本題給出push以及pop兩個list，問是否有可能組成一個合理的stack結構RU3，解題思路如下：
(a) 首先兩個指標都在起點，一個再push另一個再pop，如果當前要pop的值與push的值不同，則我們必須把push的指標往前推，直到遇到與當前
    要pop掉的數字相同為止，如果遇到了，pop的指標再往前一個，決定當前要pop的值；如果到底都遇不到，代表不可能是有效的stack(因為
    欲pop的值不存在stack中)
(b) 如果pop的指標還沒走到底(還有值需要pop)，但push指標已經到底，此時跳出while迴圈，檢查stack中是否還有剩餘的數字，如果stack空
    了，則return False(代表欲pop的數字不存在push中)，若stack頂部數字與當前要pop的值相等，我們把頂部值pop掉後依序更新當前pop值
    如果pop指標最後走到底，return True
*** 每次將pop指標往右移時，都要注意當前值是否已經到底，如果是可以提前終止，return True
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushPtr,popPtr = 0,0
        stack = []
        l_push,l_pop = len(pushed),len(popped)
        while pushPtr < l_push: # push肯定走在pop前面(如果完全相等程式內部會有pop的提前終止條件(popPtr == l_pop))
            if not stack:
                stack.append(pushed[pushPtr])
                pushPtr += 1
            popnow = popped[popPtr]
            if popnow != stack[-1]:
                while popnow != stack[-1] and pushPtr < l_push:
                    stack.append(pushed[pushPtr])
                    pushPtr += 1
                if popnow == stack[-1]:
                    stack.pop()
                    popPtr += 1
                    if popPtr == l_pop : return True # 已經pop完畢，stack中就算有剩也無妨
                else: # pushPtr == l_push
                    return False
            else:
                stack.pop()
                popPtr += 1
                if popPtr == l_pop: return True # 已經pop完畢，stack中就算有剩也無妨
        while stack: # 還沒pop完畢，只剩stack中的數字可以用(push已經用完)
            if stack[-1] == popped[popPtr]:
                stack.pop()
                popPtr += 1
            else:
                return False
        return True if popPtr == l_pop else False # 跳出while表示stack已經空掉，此時如果popPtr已經到底，則True，否則False(沒有數字可以匹配了)