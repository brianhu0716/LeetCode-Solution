# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:29:55 2021

@author: brian.hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
由右向左遍歷，只要遇到node就更新node的值以及累加和
"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(ptr) :
            if not ptr.right and not ptr.left :
                ptr.val += self.cum_sum
                self.cum_sum = ptr.val
                return
            
            if ptr.right :
                dfs(ptr.right)
            
            ptr.val += self.cum_sum
            self.cum_sum = ptr.val
            
            if ptr.left :
                dfs(ptr.left)
                
        self.cum_sum = 0
        if not root : return root
        
        dfs(root)
        return root