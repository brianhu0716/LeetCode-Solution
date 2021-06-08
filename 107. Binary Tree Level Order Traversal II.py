# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:30:16 2021

@author: brian.hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        queue,ans = [root],list()
        while queue:
            level = list()
            for i in range(len(queue)): # 預先選定本層有多少個node需要遍歷
                node = queue.pop(0) 
                level.append(node.val) # 同一層由左到右讀值
                if node.left : queue.append(node.left) # 把下一層node加入queue中
                if node.right : queue.append(node.right)
            ans = [level] + ans # 由底層往上依序列出每層的值
        return ans