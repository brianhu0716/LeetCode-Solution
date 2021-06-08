# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:48:47 2021

@author: brian.hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(ptr,val): # 由左到右依序取出node的值
            
            val.append(ptr.val)
            for next_ptr in [ptr.left,ptr.right] :
                if next_ptr:
                    dfs(next_ptr,val)
                    
            return val
        
        if not root : return root 
        val = dfs(root,list())
        
        root.left = root.right = None # 將原本root的左節點打斷
        ptr = root
        i = 1
        while i < len(val) :
            ptr.right = TreeNode(val[i]) # 將讀出來的值依序放在右節點上
            ptr = ptr.right
            i += 1