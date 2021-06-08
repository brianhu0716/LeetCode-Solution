# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:03:38 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(ptr,n):
            if not ptr.left and not ptr.right :
                if n > self.max_deep:
                    self.ans += [ptr.val]
                    self.max_deep = max(self.max_deep,n)
                return 
            
            if n > self.max_deep:
                self.ans += [ptr.val]
            for next_ptr in [ptr.right,ptr.left]:
                if next_ptr :
                    n += 1
                    dfs(next_ptr,n)
                    n -= 1


        self.max_deep = float('-inf')
        self.ans = list()
        if not root : return self.ans
        dfs(root,0)
        
        return self.ans