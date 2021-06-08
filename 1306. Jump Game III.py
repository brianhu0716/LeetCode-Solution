# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:39:57 2021

@author: Brian
"""
"""
檢測是否可以跳到任意一個值為0的index上。
本題使用動態規劃來解，當我們在任意位置時，下一步有兩個選擇 : index_now + arr[index_now] or index_now - arr[index_now]
我們透過遞迴不斷呼叫自身去解這個問題直到碰到base case 為止。 base case 如下
(a) 當目前的位置已經被走過且「知道答案」，我們直接回傳答案
(b) 當目前的位置已經超出邊界或走道已經走過的路徑上但還不知道答案(意味著形成一個循環)，return False
(c) 當arr[index] == 0 : return True

"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def helper(index,arr,visited):
            if index in self.memo.keys() : return self.memo[index] # memoization
            if not (0 <= index < len(arr)) or index in visited : return False # return False if index is out of bound or loop is detected
            if arr[index] == 0: return True   # final target
            
            visited.add(index) # record the path we've walked through
            ans = helper(index + arr[index],arr,visited) | helper(index - arr[index],arr,visited)
            
            self.memo[index] = ans
            
            return ans
        
        self.memo = dict()
        return helper(start,arr,visited = set()) 