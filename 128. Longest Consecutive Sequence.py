# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:28:33 2021

@author: Brian
"""
'''
思路：先將nums做由小到大排序，接著依次檢查是否連續
(a) 初始化存放連續長度的list為[1]，代表自己本身與自己連續
(b) 開始時(l[-1] == 1)，判斷當前index與下一個index的差值是否是1，如果是則加1，不是的話再多加一個1至l的尾部
    象徵新的一輪判斷開始
*** 如果已經在判斷當中(list[-1] != 1)，這時如果當前index與下一個index差值為0(兩數字一樣)，可以不中斷判斷
    過程，但是不能算新的數字(l[-1]不可以加1)
'''
class Solution:
    def longestConsecutive(self, nums) -> int:
        l = [1]
        nums,ln = sorted(nums),len(nums)
        for i in range(ln - 1):
            if l[- 1] == 1: # 判斷開始
                if nums[i + 1] - nums[i] == 1:
                    l[-1] = l[-1] + 1
                else:
                    l += [1]
            else: # 判斷中
                if nums[i + 1] - nums[i] == 1:
                    l[-1] = l[-1] + 1
                elif nums[i + 1] - nums[i] == 0: # [0,1,1,2]
                    continue
                else:
                    l += [1]
        
        return max(l) if ln > 0 else 0
test= Solution()
nums = [[100,4,200,1,3,2],
        [0,3,7,2,5,8,4,6,0,1],
        [0,2,0,1],
        [0,0],
        []]
for i in range(len(nums)):
    print('最多連續數字的數量為:',test.longestConsecutive(nums[i]))