# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 13:55:29 2021

@author: Brian
"""
class Solution:
    def checkPossibility(self, nums):
        false = []
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                false.append(i)
            else:
                continue
            if len(false) >= 2:  # 出現兩次遞減，無論是否連續都無法透過改一個數字變成遞增
                return False

        if not false: # 完全遞增
            return True
        elif false[0] == 0 or false[0] == l - 2: # 若錯誤位置出現在0，改成與1相同即可；又錯誤位置若在倒數第二，則改成與倒數第一即可
            return True
        '''
        如果錯誤位置(i)是在中間，我們需要確定此時是要改i 還是i + 1的值才正確，因此如果 i + 2 >= i + 1 >= i - 1(改i即可),
        若是i + 2 >= i >= i - 1(改i + 1即可)，這兩種狀況都只需要改一個值就正確
        '''
        elif nums[false[0] + 2] >= nums[false[0]] >= nums[false[0] - 1] or nums[false[0] + 2] >= nums[false[0] + 1] >= nums[false[0] - 1]:
            return True 
        else: # 若以上改法都無法滿足，則依定要改兩個值以上才正確，return False
            return False