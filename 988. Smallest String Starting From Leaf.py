# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:44:55 2021

@author: Brian
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.table = {i : string.ascii_lowercase[i] for i in range(26)}
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(ptr,s):
            if not ptr.left and not ptr.right:
                s += self.table[ptr.val]
                if not self.smallest or self.smallest > s[::-1]:
                    self.smallest = s[::-1]
                s = s[ : -1]
                return 
            
            s += self.table[ptr.val]
            for next_ptr in [ptr.left,ptr.right]:
                if next_ptr:
                    dfs(next_ptr,s)
            s = s[ : -1]
            
        self.smallest = ""
        dfs(root,"")
        
        return self.smallest