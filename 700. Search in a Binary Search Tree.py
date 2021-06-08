# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 09:42:49 2021

@author: Brian
"""


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root :return None
        
        if val > root.val:
            return self.searchBST(root.right, val)
        elif  val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root