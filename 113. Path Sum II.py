# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:33:01 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(res,ptr,cum_sum):
            if not ptr.left and not ptr.right: # leaf
                if cum_sum + ptr.val == targetSum: # 路徑總和是否等於目標值
                    self.ans += [res[:] + [ptr.val]] 
                return 
            
            res.append(ptr.val) # 還沒到leaf，繼續搜索，記錄路徑
            cum_sum += ptr.val # 更新路徑和
            for next_ptr in [ptr.left,ptr.right]: # 可以往右或往左
                if next_ptr: # 下一個節點存在時繼續搜索
                    dfs(res,next_ptr,cum_sum)
            res.pop() # 該節點已搜索完畢
            cum_sum -= ptr.val
        
        self.ans = []
        
        if not root : return self.ans # root = []
        dfs([],root,0)
        
        return self.ans