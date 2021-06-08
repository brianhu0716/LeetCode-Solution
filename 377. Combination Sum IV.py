# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:54:46 2021

@author: Brian
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(target):
            if target in self.memo.keys() : return self.memo[target]
            
            if target == 0 : return 1
            
            if target < 0 : return 0
            
            
            ans = 0
            for num in nums:
                ans += dfs(target - num)
            self.memo[target] = ans
            
            return ans
        
        self.memo = dict()
        return dfs(target)
        '''
        def dfs(total):
            if sum(total) > target :
                return 
            if sum(total) == target:
                ans.append(total[:])
                return 
            
            for idx in range(n):
                total.append(nums[idx])
                dfs(total)
                total.pop()
            return 
        n,ans = len(nums),list()
        dfs([])
        return len(ans)
        '''