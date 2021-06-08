# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:26:23 2021

@author: Brian
"""
'''
本題的解題思路如下:
(a. 首先必須要知道該序列已經呈現ascending sorted的情況，只是不知道是否有rotate過，又因為我們只需要知道target
     是否有出現在序列中，因此我們不再還原沒有rotate過的序列，而是直接用頭尾的值來決定要從何處搜索較快
     (a.1 若尾部值(nums[-1])"大於"頭部值(nums[0]):代表該序列沒被旋轉過或是剛好轉回原點，因此若是target比尾部值大
          或比頭部值小，表示目標不在序列之間(因為ascending sorted過)。若在頭尾值之間，我們再判斷目標值與尾部值接近
          還是與頭部值接近，若接近頭部值則由index = 0開始找比較快，反之由index = -1找較快
     (a.2 若尾部值(nums[-1])"小於"頭部值(nums[0]):此種情況代表被rotate過，因此我們直接判斷目標值是否比頭部值大、
          或是比尾部值小，如果是比頭部值大則由index = 0開始搜索較快，若比尾部值小則由index = -1開始搜索較快
          如果目標值卡在[尾部值,頭部值+1]之間代表目標不存在(因為是ascending order)
'''
class Solution:
    def search(self, nums, target):
        if nums[-1] > nums[0]: # 已經是ascending order了(沒有rotate)
            if target > nums[-1]:
                return -1
            elif target < nums[0]:
                return -1
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
                return -1
                
                    
       
    def backwardSearch(self,nums,target):
        for i in range(len(nums) - 1, -1,-1):
            if target == nums[i]:
                return i
            elif target < nums[i]:
                if i - 1 >= 0: # 避免len(nums) == 1, nums = [1],target = 0
                    continue
                else:
                    return -1
            else:
                return -1
    def forwardSearch(self,nums,target):
        for i in range(0,len(nums),1):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                if i + 1 <= len(nums) - 1: # 避免len(nums) == 1,nums[1],target = 2 
                    continue
                else:
                    return -1
            else:
                return -1

