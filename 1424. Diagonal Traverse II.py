# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:21:48 2021

@author: Brian
"""
'''
第一種方法：找規律
每次matrix拿對角線的方法都是由上往下、由左往右，如果我們拿完後就將元素刪除，會發現永遠都只需要拿第0個值(不必考慮
左右的問題了)，每一輪做完c就加1，一直做到nums的最大邊界為止，在拿的過程中每一個範圍內的row都會依次拿掉一個元素，
只要發現這個nums[row]空掉，就刪除且c在減1(壓縮最大邊界)，直到nums完全空掉為止
第二種解法：矩陣特性
拿對角線元素時，他們的row + col值一定會相等，因此我們由第0個row開始拿，由左往右，並將每個元素的行加列值當作key
存在字典中，依次拿到最後一個row，其中有相等的key值元素代表它在同一個對角線上，只要append到同key值的list中即可，
最後將key值sort後由小到大取出list的值(list的值要倒過來，因為我們scan的時候是由上往下，但題目要求是由下往上)

'''
nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
nums = [[1,2,3,4,5,6]]

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        c = 0
        diag = []
        while nums:
            for row in range(c,-1,-1):
                diag.append(nums[row].pop(0))
                if not nums[row]:
                    del nums[row]
                    c -= 1
            (c := c + 1) if c < len(nums) - 1 else c
        return diag
        '''
        row,d,diag = len(nums),defaultdict(list),list()
        for i in range(row):
            for j in range(len(nums[i])):
                d[i + j].append(nums[i][j])
        for key in sorted(d.keys()):
            diag += d[key][::-1]
        return diag
        '''