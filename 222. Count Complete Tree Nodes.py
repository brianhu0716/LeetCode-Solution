# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:51:09 2021

@author: brian.hu
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(ptr) :
            self.ans += 1
            for next_ptr in [ptr.left,ptr.right] :
                if next_ptr : 
                    dfs(next_ptr)

        if not root : return 0
        self.ans = 0
        dfs(root)
        return self.ans