# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:23:53 2021

@author: Brian
"""
'''
本題的解題思路與第33題相同，不再贅述
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums[-1] > nums[0]: # 已經是ascending order了(沒有rotate)
            if target > nums[-1]:
                return False
            elif target < nums[0]:
                return False
            else:
                if nums[-1] - target < target - nums[0]: # 判斷靠近頭還是尾
                    return self.backwardSearch(nums,target)
                else:
                    return self.forwardSearch(nums,target)
        else: # 原序列有rotate過
            if target <= nums[-1]: # 
                return self.backwardSearch(nums,target)
            elif target >= nums[0]:
                return self.forwardSearch(nums,target)
            else:
                return False
                
                    
       
    def backwardSearch(self,nums,target):
        for i in range(len(nums) - 1, -1,-1):
            if target == nums[i]:
                return True
            elif target < nums[i]:
                if i - 1 >= 0: # 避免len(nums) == 1, nums = [1],target = 0
                    continue
                else:
                    return False
            else:
                return False
    def forwardSearch(self,nums,target):
        for i in range(0,len(nums),1):
            if target == nums[i]:
                return True
            elif target > nums[i]:
                if i + 1 <= len(nums) - 1: # 避免len(nums) == 1,nums[1],target = 2 
                    continue
                else:
                    return False
            else:
                return False