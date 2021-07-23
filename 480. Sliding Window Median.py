# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:37:25 2021

@author: Brian Hu
"""

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
		# res keep the sequence from i - k + 1 to i, we need to find the median when the i varies from k to len(nums) - 1
        res = sorted(nums[: k])
        median = res[k // 2] if k % 2 == 1 else sum(res[k // 2 - 1: k // 2 + 1]) / 2
        ans = [median]
        for idx in range(k, len(nums)):
            rmv, add = nums[idx - k], nums[idx] # for any idx, we need to remove nums[idx - k] from previous res and add nums[idx] to previous res to make current res
            i, j = 0, k - 1
            while i <= j: # the first binary search is to find the index where the value should be removed
                mid = (i + j) // 2
                if res[mid] > rmv:
                    j = mid - 1
                elif res[mid] < rmv:
                    i = mid + 1
                else:
                    res = res[: mid] + res[mid + 1:]
                    break
            i, j = 0, k - 2
            while i <= j: # the second is to insert the current number to sequence
                mid = (i + j) // 2
                if res[mid] > add:
                    j = mid - 1
                else:
                    i = mid + 1
            res.insert(i, add)
            ans.append(res[k // 2] if k % 2 == 1 else sum(res[k // 2 - 1: k // 2 + 1]) / 2)
        return ans