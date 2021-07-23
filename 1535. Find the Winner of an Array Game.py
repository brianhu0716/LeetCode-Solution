# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:54:11 2021

@author: Brian Hu
"""

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i, n = 0, len(arr)
        while i < n - 1:
            cnt = 0 if i == 0 else 1 # any start value arr[i] except arr[0] is at least bigger than the value of arr[i - 1]
            if cnt == k: # meet the requirement
                return arr[i]
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    cnt += 1 # cnt counts the consecutive length of arr[i] > arr[j]
                else:
                    i = j # arr[i] < arr[j], the next round is start at index j
                    break
                if cnt == k: # check whether the requirement is met
                    return arr[i]
            if j == n - 1: # because it is guaranteed to have one solution, the arr[i] must be the answer!!!
                return arr[i]