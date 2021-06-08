# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:58:57 2021

@author: brian.hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(ptr) :
            if not ptr : return 
            
            inorder(ptr.left) 
            
            self.val.append(ptr.val)
            
            inorder(ptr.right)
        
        self.val = list()
        inorder(root)
        
        return self.val