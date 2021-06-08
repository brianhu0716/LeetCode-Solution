# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:12:14 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 與113類似
class Solution:
    def pathSum(self, root: TreeNode, targetSum : int) -> int:
        def checkEqual(path,cum_sum): # 判斷路徑中是否有滿足目標和的路徑
            if cum_sum == targetSum : self.ans += 1
            for idx in range(l := len(path)) :
                if idx == l - 1:
                    break
                cum_sum -= path[idx]
                if cum_sum == targetSum : 
                    #print(path[idx + 1 : ])
                    self.ans += 1
            return 
        
        def dfs(path,cum_sum,ptr):
            if not ptr.left and not ptr.right: # leaf
                checkEqual(path + [ptr.val],cum_sum + ptr.val)
                return 
            
            path.append(ptr.val)
            cum_sum += ptr.val
            checkEqual(path,cum_sum) # 每增加一個節點就要確認路徑中是否有滿足target的和
            for next_ptr in [ptr.left,ptr.right]:
                if next_ptr : # 節點存在才繼續做深度優先搜索
                    dfs(path,cum_sum,next_ptr)
            path.pop()
            cum_sum -= ptr.val
            
        self.ans = 0
        if not root : return self.ans
        
        dfs([],0,root)
        return self.ans