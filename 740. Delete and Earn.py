# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:29:19 2021

@author: Brian
"""
"""
與小偷偷房子問題類似，我們在考慮當前數字為num可以取到的最大值，其值應分以下兩種狀態討論
(a) 如果num 有出現在nums中，則最大值 = max(num * num 出現的次數 + num - 2 * num - 2 出現的次數 , num - 1 * num - 1 出現的次數)
(b) 如果num 沒有出現在nums中，num 出現的次數為0，所以最大值 = max(num * 0 + num - 2 * num - 2 出現的次數 , num - 1 * num - 1 出現的次數)
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = dict()
        for num in nums:
            table[num] = table.get(num,0) + 1 # count the frequency of each distinct number in nums
        dp = [0 for i in range(max(table.keys()) + 1)] 
        for num in range(len(dp)):
            if num in table.keys():
			# trasition 1 : if num in table.keys(), we take the maximum of  num * freq of num + (num - 2) * freq of (num - 2) and (num - 1) * freq of (num - 1) 
                dp[num] = max(num * table[num] + dp[num - 2] , dp[num - 1])  
            else:
			# transition 2: because num doesn't show up in nums, the term in transition 1 : num * freq of num --> 0. we need to take the maximum of (num - 1) * freq of (num - 1) and (num - 2) * freq of (num - 2)
                dp[num] = max(dp[num - 1] , dp[num - 2])
        #print(dp)
        return dp[-1]