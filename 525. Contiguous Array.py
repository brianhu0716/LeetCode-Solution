# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:38:26 2021

@author: brian.hu
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cum_sum = 0
        max_len = 0
        table = {0 : -1}
        for idx,num in enumerate(nums) :
            cum_sum = cum_sum - 1 if num == 0 else cum_sum + 1
            if cum_sum not in table : # 將當前的前綴和以及位置加入字典
                table[cum_sum] = idx
            else : # 如果出現相同的前綴和，則計算當前位置與最初前綴和位置的距離
                max_len = max(max_len,idx - table[cum_sum])
        return max_len