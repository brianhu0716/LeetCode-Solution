# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:34:27 2021

@author: Brian
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valide(node,minval,maxval):
            if not node:return True
            if node.val <= minval or node.val >= maxval : return False
            #print(node.val,minval,maxval)
            return valide(node.left,minval,node.val) and valide(node.right,node.val,maxval)
            
        return valide(root,float('-inf'),float('inf'))