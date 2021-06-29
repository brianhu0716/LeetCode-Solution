# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:43:09 2021

@author: Brian Hu
"""
'''
(a) first, we need to guarantee arr length == n and every entry is start by minima positive integer 1, and since we can tolerate abs(arr[i] - arr[i + 1]) <= 1, we can further assume the target = arr[index] start by 2. Based on previous concept, the remaining maxSum we can actually be used to optimized is maxSum -= n - 1
(b) in while loop, j and i represent the max index and min index which define the range we need to optimize in current iteration. Every entry in the range must add by 1, so maxSum = maxSum - (j - i + 1) and target can be added by 1.
(c) we repeat (b) until maSum is no longer enough big to optimize every entry in rangr(i, j + 1), or j and i have already reached the bounds of array size, in this case, we can reduction the remaining process to count target + maxSum // (j - i + 1) as the answer because the optimization range is fixed in the remaining process
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if maxSum == n: return 1
        i, j = max(0, index - 1), min(index + 1, n - 1)
        target = 2
        maxSum -= (n + 1)
        while maxSum >= (j - i + 1):
            maxSum -= j - i + 1
            target += 1
            if i > 0 and j < n - 1:
                i -= 1
                j += 1
            elif i == 0 and j == n - 1:
                return target + maxSum // (j - i + 1)
            elif i == 0 and j < n - 1:
                j += 1
            elif i > 0 and j == n - 1:
                i -= 1
        return target