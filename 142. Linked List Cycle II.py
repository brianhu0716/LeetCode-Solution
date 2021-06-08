# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:15:13 2021

@author: Brian
"""
'''
利用快慢指標，假設快指標的移動速度是慢指標的兩倍，又當前的連結串列為一條長度a的單向串列加上長度c的環形串列，假設兩指標都從head
開始移動，進入環形區域後曼指標一定會被愾指標追上，理由如下：假設慢指標已經走了slow = a + d的距離；快指標一定是走了a + d + c * n
的距離兩指標才會第一次相遇，又塊指標的速度是曼指標的兩倍，因此有 2 * (a + d) = a + d + c * n的關係存在，化減後可得：
a = c * n - d = n * (c - d + d) - d = (n - 1) * d + n * (c - d) = (n - 1) * d + (n - 1) * (c - d) + (c - d)，最後得到
a = (n - 1) * c + (c - d)。也就是說如果有一個特別的指標，他一開始就在快慢指標第一次相遇的位置繞圈移動，當它繞了(n - 1)圈後只要
再移動 c - d 的距離就可已回到環形的起始點
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        data_seen = list()
        while head:
            if head not in data_seen:
                data_seen.append(head)
                head = head.next
            else:
                return head       
        return head
        '''
        fastptr,slowptr = head,head
        while True:
            if not fastptr or not fastptr.next: return None
            
            fastptr,slowptr = fastptr.next.next,slowptr.next
            
            if slowptr == fastptr: break
                
        startptr = head
        while startptr != slowptr:
            startptr = startptr.next
            slowptr = slowptr.next
        return slowptr