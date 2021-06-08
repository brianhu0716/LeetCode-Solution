# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:58:03 2021

@author: Brian
"""
'''
將指定範圍內的子數列sorted後找出參考差，接著遍歷子數列，只要任一相鄰數字差不等於參考差回傳false，否則true
'''
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = list()
        for i in range(len(l)):         
            test = sorted(nums[l[i]:r[i] + 1])
            ref = test[1] - test[0]
            all_same = True
            for j in range(0,len(test) - 1):
                if test[j + 1] - test[j] != ref:
                    ans.append(False)
                    all_same = False
                    break
            if all_same : ans.append(True)
        return ans