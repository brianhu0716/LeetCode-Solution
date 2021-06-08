# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:50:29 2021

@author: brian.hu
"""
"""
與102,107題類似
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        queue = [root]
        ans = list()
        nlayer = 0
        while queue :
            level = list()
            for i in range(len(queue)) :
                node = queue.pop(0)
                level.append(node.val)
                for next_node in [node.left,node.right] :
                    if next_node :
                        queue.append(next_node)
            if nlayer % 2 == 1:
                level = level[::-1]
            ans.append(level)
            nlayer += 1
        return ans