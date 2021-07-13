# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:15:17 2021

@author: Brian Hu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def removeRepeat(arr, start, end, flag):
            for i in range(start, end):
                if arr[i] != flag:
                    return i
            return end
        arr = list()
        while head:
            arr.append(head.val)
            head = head.next
        i = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i + 1]:
                j = removeRepeat(arr, i + 2, len(arr), arr[i])
                arr = arr[: i] + arr[j: ]
            else:
                i += 1
        if not arr:
            return None
        head = ListNode(arr[0])
        ptr = head
        for i in range(1, len(arr)):
            ptr.next = ListNode(arr[i])
            ptr = ptr.next
        return head
        