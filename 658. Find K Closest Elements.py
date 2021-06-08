# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:54:06 2021

@author: brian.hu
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        p1, p2 = 0, n - 1
        while p1 <= p2: # binary search 可以找到最後最接近target的位置(不一定等於target)
            mid = int((p1 + p2) // 2)
            if arr[mid] < x: 
                p1 = mid + 1
            elif arr[mid] > x: 
                p2 = mid - 1
            else: break 
                
        low, high = mid - 1, mid
        ans = deque()
        for _ in range(k): 
            if low == -1 : # 無法再往左
                ans.append(arr[high])
                high += 1
            elif high == n : # 無法再往右
                ans.appendleft(arr[low])
                low -= 1
            elif abs(arr[low] - x) > abs(arr[high] - x) :
                ans.append(arr[high])
                high += 1
            elif abs(arr[low] - x) <= abs(arr[high] - x) :
                ans.appendleft(arr[low])
                low -= 1
        return ans 