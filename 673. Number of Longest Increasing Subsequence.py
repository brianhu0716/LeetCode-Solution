# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:29:39 2021

@author: Brian
"""
'''
與第300以及334題類似
'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1 for _ in nums]
        table = [{1 : 1} for i in range(l)]
        for i in range(0,l):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j] + 1:
                        dp[i] = max(dp[i],1 + dp[j])設成key
                        # 將更新後的長度加入table[i]中，且必須累積table[j]中長度為dp[j]的個數
                        table[i][dp[i]] = table[i].get(dp[i],0) + table[j][dp[j]] 
                    else:
                        continue
                    #print(i,j,table[i])
        #print(dp)
        #print(table)
        
        max_length_now = list()
        for sub_table in table:
            max_length_now.append(max(sub_table.keys()))
        global_max_length = max(max_length_now)
        idx = [True if max_length_now[i] == global_max_length else False for i in range(l)]
        #print(idx)
        
        return sum([table[i][global_max_length] for i in range(l) if idx[i] == True])
    
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        table = [{1 : 1} for _ in nums]
        for i in range(0,l := len(nums)):
            for j in range(i - 1,-1,-1):
                if nums[i] > nums[j]:
                    table[i][1 + dp[j]] = table[i].get(1 + dp[j],0) + table[j][dp[j]]
                    dp[i] = max(1 + dp[j],dp[i])
        #print(dp)
        #print(table)
        local_max_len = [max(t.keys()) for t in table]
        max_idx = [True if local_max_len[i] == (global_max_len := max(local_max_len)) else False for i in range(l)]
        
        return sum([table[i][global_max_len] for i in range(l) if max_idx[i] == True])
"""