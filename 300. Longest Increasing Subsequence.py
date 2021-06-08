# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:39:33 2021

@author: Brian
"""
'''
本題不去確定的因素為：不知道是否要將第i個元素納入考量。為了確保無後效應，我們將這個不確定狀態確定下來，並維持該狀態優化小問題，
並透過迭代求得整個問題的最佳解。思路如下：

(a) 首先初始化dp array，個元素的值都為1，代表最初時每個遞增序列只包含自己一個元素。而dp[i]的值代表到第i個數字為止最長的遞增子序列長度
(b) 外部迴圈由index = [0,len(nums)] 開始迭代，接著內部迴圈迭代由index 0 開始到當前的i(注意：優化時必須包含i)中所有的數字，
    將這些數字逐一與nums[i]做比較    只要nums[j] < nums[i] 代表dp[i]的長度可以多一個(此時遞增序列為nums[j],nums[i])，內部回
    圈每一動一個index只要滿足nums[j] < nums[i]我們就更新一次dp[i]。
(c) 最後回傳答案並非是dp[-1]，而是dp array中值最大的數字(代表到該位置的遞增子序料長度最長)

'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        for i in range(0,len(nums)):
            for j in range(0,i): # index before index i
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],1 + dp[j])
        
        return max(dp)