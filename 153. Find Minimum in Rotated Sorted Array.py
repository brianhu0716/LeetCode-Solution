# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:10:25 2021

@author: Brian
"""
'''
rotated sorted array 指一個陣列本身已被ascending sorted,然後又被旋轉了k次,
本題希望能找出這個rotated sorted array中最小的值，演算法如下：
(a. 因為我們不知道被旋轉了幾次，因此直接從index = 0往後找，只要發現中間突然從一路上升值變下降值時，該下降值即
     為最小值
(b. 若從index = 0 至index = -1都找不到該值，代表該序列被轉回原始樣子(即k = len(nums) * n(n屬於正整數))，此時直接
     判定定第一個為值值為最小值
(c. 以flag旗標來判別最小值是否出現在[1,len(nums)]或是[0]
'''
class Solution:
    def findMin(self, nums) -> int:
        flag = False
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                flag = True
                break
        if flag:
            return nums[i + 1]
        else:
            return nums[0]