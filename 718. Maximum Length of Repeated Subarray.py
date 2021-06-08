# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:53:39 2021

@author: brian.hu
"""
"""
dp[i][j]定義為nums1[i :]以及nums2[j :]間最長的共同字串長度
對於任一狀態nums1[i] == nums2[j]時，dp[i][j]的最長共同子字串長度由dp[i][j]或是
dp[i + 1 :][j + 1 :] + 1來決定
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        
        for i in range(len(nums1) - 1,-1,-1) :
            for j in range(len(nums2) - 1,-1,-1) :
                if nums1[i] == nums2[j] :
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    
        return max((max(row) for row in dp))