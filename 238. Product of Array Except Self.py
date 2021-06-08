# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:44:11 2021

@author: Brian
"""
'''
解題思路：分三種情況
(a) 如果nums中至少有2個0，則無論是哪一個元素其不包含自己的乘積一定都是0
(b) 如果只有一個0，則當自己是0時不包含自己的乘積是其餘數字的乘積
(c) 如果沒有0則把所有數字的乘積除以自己後取"商"(一定可以整除)，即為不包含自己的乘積
***我們在判斷有幾個0時，最多找到2個0即可提前終止搜索，因為無論之後有幾個0，即使計算時當前數字是0，排除自己後
    還是會有一個0強迫不包含自己的乘積為0
***如果只有1個或0個0則經繼續累乘

'''
class Solution:
    def productExceptSelf(self, nums):
        i0,total = 0,1
        for n in nums:
            (i0 := i0 + 1) if n == 0 else i0
            if i0 == 2:
                break
            else:
                (total := total * n) if n != 0 else total
        if i0 == 2:
            product = [0 for n in nums]
        elif i0 == 1:
            product = [0 if n != 0 else total for n in nums]
        else:
            product = [total / n for n in nums] # //:取商即可，避免結果為float
        return product


test = Solution()
nums = [[1,2,3,4],
        [-1,1,0,-3,3],
        [0,4,0],
        [0,0]]
for n in nums:
    print(test.productExceptSelf(n))