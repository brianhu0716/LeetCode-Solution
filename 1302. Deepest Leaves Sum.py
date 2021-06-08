# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:05:13 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(N,ptr):
            for next_ptr in [ptr.left,ptr.right]:
                if next_ptr == None :
                    if N > self.ans[0] : self.ans = [N,ptr.val]
                    elif N == self.ans[0] : self.ans[1] += ptr.val
                    #print(ptr.val,self.ans)
                else:
                    dfs(N + 1,next_ptr)
        self.ans = [float('-inf'),0]
        dfs(0,root)
        return self.ans[1] // 2