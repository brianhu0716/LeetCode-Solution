# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:15:42 2021

@author: brian.hu
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        ptr = head
        self.val = list()
        while ptr :
            self.val.append(ptr.val)
            ptr = ptr.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.val)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()