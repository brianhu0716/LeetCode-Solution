# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:26:59 2021

@author: Brian
"""
'''
序列中有0,1,2種元素，目標是把序列sort後列出，我們只要檢視相鄰的兩個數字，只要前一個數字大於後一個，就交換位置
並設定一個旗標all_fixed，如果序列中有發生交換位置，該旗標為False繼續執行sort的動作，如果該旗標為True代表序列
已經呈現遞增的狀態，即可停止排序
'''
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        while True:
            all_fixed = True 
            for i in range(l - 1):
                if nums[i] > nums[i + 1]:
                    nums[i + 1],nums[i] = nums[i],nums[i + 1]
                    all_fixed = False
            if all_fixed:
                break