# -*- coding: utf-8 -*-
"""
Created on Mon May 24 08:46:27 2021

@author: brian.hu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ptr = head
        val = list()
        while ptr :
            val.append(ptr.val)
            ptr = ptr.next
        ptr = head
        val = sorted(val)
        for i in range(len(val)):
            ptr.val = val[i]
            ptr = ptr.next
        return head