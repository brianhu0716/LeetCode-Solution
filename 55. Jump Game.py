# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:21:18 2021

@author: Brian
"""
class Solution:
    def canJump(self, nums) -> bool:
        p = 0
        ln = len(nums) - 1    
        while True :
            if nums[p] != 0: # 位移量不等於0時
                if p + nums[p] >= ln: # 可直接到達終點
                    return True
                else:
                    for i in range(p + 1,p + nums[p] + 1): # 在當前位置以及該位置加最大位移量的範圍內搜索
                        if i + nums[i] >= p + nums[p]: # 如果範圍內有位置的位移量加位置值大於當前值，則將為值移動到該處等號-->[3,2,1,0,4]
                            p = i # 
                            if p + nums[p] >= ln: #移動後做判斷，若可以直接到達終點則結束程式
                                return True
            else: # 當移動到一位置的位移量是0時
                if ln != 0: # 如果該數列的長度大於1，則不可能到達終點
                    return False
                else:
                    return True