# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:02:01 2021

@author: Brian
"""

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        need = goal - sum(nums) # 實際值與目標值的差 = 需要值
        if abs(need) > limit: # 如果需要值大於限制，每次只能加上最多限制次數的值
            mod = abs(need) % limit
            return abs(need)// limit + 1 if mod != 0 else abs(need)// limit # 最後一次如果不夠拿完還要在加1
        else:
            return 1 if need != 0 else 0 # 如果需要值是0，不必再拿一次