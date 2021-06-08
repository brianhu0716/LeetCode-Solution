# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:41:31 2021

@author: brian.hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
採用inorder的方式讀值，並在呼叫next時一一取出
"""
class BSTIterator:

    def __init__(self, root: TreeNode):
        def inorder(ptr) :
            if not ptr : return 
            
            inorder(ptr.left)
            self.inorder.append(ptr.val)
            inorder(ptr.right)
            
        self.inorder = list()
        inorder(root)
        
        self.count = 0
        self.len = len(self.inorder)
    def next(self) -> int:
        ans = self.inorder[self.count]
        self.count += 1
        return ans
            
    def hasNext(self) -> bool:
        if self.count < self.len : return True
        return False