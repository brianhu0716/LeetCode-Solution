# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:32:08 2021

@author: Brian Hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dq, count = deque([root]), 0
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                common = False
                if node.val in [x, y]:
                    count += 1
                if node.left:
                    if node.left.val in [x, y]:
                        common = True
                    dq.append(node.left)
                if node.right:
                    if node.right.val in [x, y]:
                        if common: # has common parents
                            return False
                    dq.append(node.right)            
            if count == 1: # not in the same depth
                return False
            if count == 2: # in the same depth and have different parents
                return True