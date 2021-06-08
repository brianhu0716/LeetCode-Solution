# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:19:02 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(ptr,s):
            if not ptr.left and not ptr.right:
                self.total += int(s + str(ptr.val))
                return
            
            s += str(ptr.val)
            for next_ptr in [ptr.left,ptr.right]:
                if next_ptr:
                    dfs(next_ptr,s)
            s = s[ : len(s) - 1]
        
        self.total = 0
        dfs(root,"")
        
        return self.total