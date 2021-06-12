# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:02:04 2021

@author: Brian Hu
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod, ans, p1 = 1, 0, 0
        for p2 in range(len(nums)):
            prod *= nums[p2]
            while prod >= k :
                prod /= nums[p1]
                p1 += 1
            ans += p2 - p1 + 1 # # of combinations in the range [left,right]
        return ans

"""
ex: [10,5,2,6] k = 100
p1 = 0, p2 = 0 --> prod = 10 < k ans = 1 ([10]) 
p1 = 0, p2 = 1 --> prod = 50 < k ans = 1 + 2 ([10,5],[5])
p1 = 0, p2 = 2 --> prof = 100 < k 
    --> p1 = 1, p2 = 2 --> prod = 10 < k ans = 1 + 2 + 2 ([5,2],[2])
p1 = 1, p2 = 3 -- > prod = 60 < k ans = 1 + 2 + 2 + 3 ([5,2,6],[2,6],[6])

"""