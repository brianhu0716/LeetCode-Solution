# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:04:50 2021

@author: Brian
"""
'''
Arithmetic的定義為：數列中至少有三個數字，數字以及數字之間的差固定，本題要求計算最多有多少個Arithmetic 子數列
'''
class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        def findend(start,l,nums,ref):
            for i in range(start,l - 1):
                if (nums[i + 1] - nums[i]) != ref:
                    return i
            return l - 1

        if (l := len(nums)) < 3: return 0
        elif l == 3: return 1 if (nums[2] - nums[1]) == (nums[1] - nums[0]) else 0
        start = 0
        self.n = 0
        while start + 2 < l:
            if (ref := nums[start + 2] - nums[start + 1]) == nums[start + 1] - nums[start]:
                i = findend(start + 2,l,nums,ref)
                self.n += (1 + (i - start + 1 - 2)) * (i - start + 1 - 2) * 0.5
                start = i
            else:
                start += 1
        return int(self.n)
test = Solution()
nums = [[1,2,3,4],
        [1],
        [1,2,3,8,9,10],
        [1,2,3]
        ]
for n in nums:
    print(test.numberOfArithmeticSlices(n))