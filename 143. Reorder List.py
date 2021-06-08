# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:10:13 2021

@author: brian.hu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ptr = head.next
        dq = collections.deque()
        while ptr :
            dq.append(ptr.val)
            ptr = ptr.next
        
        ptr = head.next
        for i in range(len(dq)) :
            if i % 2 == 0 :
                ptr.val = dq.pop()
            else :
                ptr.val = dq.popleft()
            ptr = ptr.next
        return head