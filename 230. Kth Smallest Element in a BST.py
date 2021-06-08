# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:27:03 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def dfs(ptr): # 走訪所有的node，最後把值排序後印出地k個即可
            if not ptr:
                return 
            
            self.ans += [ptr.val]
            for next_ptr in [ptr.left,ptr.right]:
                dfs(next_ptr)
        
        self.ans = list()
        dfs(root)
        return sorted(self.ans)[k - 1]