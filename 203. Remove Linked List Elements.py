# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:53:48 2021

@author: Brian
"""
'''
這一題需要考慮到如果一開始(head)就是val的情況，我們必須要把head先移動到期val不等於val的情況再操作
(a) 由於一開始時如果就是val我們勢必要傳此節點，但由於它的位置是在頭部，因此只要把head定為head.next就等於刪除原本的head了
(b) 等到第一次出現head.val不等於val時，我們把當前的head設定為ptr(因為ptr之後的動作可以同時更動到head)，接者只需移動ptr即可
    移動方法為當下一個val(ptr.next.val)為val時，我們把ptr.next設定為ptr.next.next即等效於刪除原先ptr.next的資料，同時"ptr不可以動"
    因為不確定下一個資料是否也等於val，如果不是的話ptr就往前移動一個位置
*** key:確保當前的ptr.val永遠都不會等於val
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode: 
        if not head: return head
        while head.val == val:
            head = head.next  
            if not head: return head
        ptr = head
        while ptr and ptr.next:
            '''
            確保當前的ptr.val永遠都不會等於val
            '''
            if ptr.next.val == val: # ptr的下一個資料的val等於val
                ptr.next = ptr.next.next
            else: # 如果不是則ptr可以往下一格
                ptr = ptr.next
        return head