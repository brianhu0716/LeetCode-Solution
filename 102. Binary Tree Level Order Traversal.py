# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:59:01 2021

@author: brian.hu
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""" BFS solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        queue = [root]
        ans = list()
        while queue :
            level = list()
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                for next_node in [node.left,node.right]:
                    if next_node :
                        queue.append(next_node)
            ans.append(level)
        return ans
"""
'''DFS solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        def dfs(ptr,level) :
            self.table[level].append(ptr.val)
            for next_ptr in [ptr.left,ptr.right] :
                if next_ptr :
                    dfs(next_ptr,level + 1)
        
        self.table = collections.defaultdict(list)
        dfs(root,0)
        return [self.table[level] for level in sorted(self.table.keys())] 
'''