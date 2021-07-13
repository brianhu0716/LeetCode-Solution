# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:11:14 2021

@author: Brian Hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def addNode(node, direction, val):
            if direction == 'left':
                temp = node.left
                node.left = TreeNode(val)
                node = node.left
                node.left = temp 
            else:
                temp = node.right
                node.right = TreeNode(val)
                node = node.right
                node.right = temp
            return 
        if depth == 1:
            temp = root
            root = TreeNode(val)
            root.left = temp
            return root
        nodes = deque([root])
        level = 1
        while nodes:
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if level != depth - 1:
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                else:
                    if node.left:
                        addNode(node, 'left', val)
                    else:
                        node.left = TreeNode(val)
                    if node.right:
                        addNode(node, 'right', val)
                    else:
                        node.right = TreeNode(val)
            level += 1
        return root