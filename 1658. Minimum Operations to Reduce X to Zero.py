# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:38:20 2021

@author: Brian
"""
'''
本題可以將題意轉換為找出最長的序列使得其總和等於元序列總和減去目標值,因此一樣利用兩個指標進行運作，右指標先移動，每一棟一個位置
就將當前的累積和上加，如果當前累積和等於與尋找的值時，更新一次長度，如果當前的累積和大於欲尋找的值，就移動左指標，值到小於欲尋
找的目標值，若等於的話，再更新一次長度。依此邏輯重複進行，值到右邊界碰到序列尾端為止。最終答案為元序列長度減去尋到的最大長度，
如果搜尋到的最大長度等於無窮大(預設值)，代表目標不存在，回傳-1
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        x = sum(nums) - x
        lp,lx,cur_sum,lt = 0,float('-inf'),0,len(nums)
        if x == 0:
            return lt
        for rp in range(lt):
            cur_sum += nums[rp]
            if cur_sum == x:
                lx = max(lx,rp - lp + 1)
            elif cur_sum > x:
                while cur_sum > x and lp < rp:
                    cur_sum -= nums[lp]
                    lp += 1
                if cur_sum == x:
                    lx = max(lx,rp - lp + 1)
            else:
                continue
        return lt - lx if lx != float('-inf') else -1