# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:09:49 2021

@author: Brian Hu
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(arr, ptr, direction):
            if direction == 'left': # build left children of ptr
                if arr: # still have some number can be selected
                    imax = arr.index(max(arr))
                    ptr.left = TreeNode(arr[imax])
                    dfs(arr[: imax], ptr.left, 'left') 
                    dfs(arr[imax + 1:], ptr.left, 'right')
                else: # no option to build node, ptr is a leaf
                    ptr.left = None
                    return 
            else: # build right children of ptr
                if arr:
                    imax = arr.index(max(arr))
                    ptr.right = TreeNode(arr[imax])
                    dfs(arr[: imax], ptr.right, 'left')
                    dfs(arr[imax + 1:], ptr.right, 'right')
                else:
                    ptr.right = None
                    return
        imax = nums.index(max(nums))
        head = TreeNode(nums[imax])
        ptr = head
        dfs(nums[: imax], ptr, 'left')
        dfs(nums[imax + 1: ], ptr, 'right')
        return head