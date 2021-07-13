# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:12:58 2021

@author: Brian Hu
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            self.d[num].append(idx)

    def pick(self, target: int) -> int:
        lst_idx = self.d[target]
        idx = random.randint(0, len(lst_idx) - 1)
        return lst_idx[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)