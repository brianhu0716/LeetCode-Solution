# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:43:03 2021

@author: brian.hu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        l = list()
        cnt = 1
        ptr = head
        while cnt <= right : # 找出要反向的連結串列
            if cnt >= left :
                l.append(ptr)
            cnt += 1
            ptr = ptr.next
        lp,rp = 0,len(l) - 1
        # 利用左右指標，每次都將左指標以及右指標的val交換，直到右指標值小於左指標值為止
        while rp > lp :
            node_left,node_right = l[lp],l[rp]
            node_left.val ,node_right.val = node_right.val ,node_left.val
            rp -= 1
            lp += 1
        return head