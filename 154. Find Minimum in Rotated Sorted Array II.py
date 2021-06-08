# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:55:25 2021

@author: Brian
"""
'''
如果mid等於high，由於不知道極小值發生在mid之前或mid之後([1,0,1,1,1],[1,1,1,0,1])，只能由high - 1依次判斷，又如果是high - 1的話
必須考慮現在的high位置對應的值是否有可能是唯一極小值-->答案顯然是不會的，因為與當前狀況相悖(mid與high相等),

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:        
        low,high = 0,len(nums) - 1     
        while low < high:
            mid = ((low + high) // 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid # 不能減1，因為最小值可能是現在的mid
            else: 
                high -= 1 
        return nums[low]
        
        '''
        flag = False
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                flag = True
                break
        return nums[i + 1] if flag else nums[0]

        
    