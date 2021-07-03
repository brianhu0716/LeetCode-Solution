# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:29:00 2021

@author: Brian Hu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, ans = list(), list()
        idx = 0
        while head:
            if not stack:
                stack.append([idx, head.val])
            else:
                while stack and head.val > stack[-1][1]: # find the first greater number
                    stack[-1][1] = head.val
                    ans.append(stack.pop())
                stack.append([idx, head.val])
            head = head.next
            idx += 1
        while stack: # the remaining number in stack don't have any number greater than them
            stack[-1][1] = 0
            ans.append(stack.pop())
        ans.sort()
        return [ans[i][1] for i in range(idx)] # retrieve the first greater number as final answer