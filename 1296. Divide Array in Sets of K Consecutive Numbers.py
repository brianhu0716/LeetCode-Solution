# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:28:31 2021

@author: Brian Hu
"""
"""
share the same concept of #846, at first, we count num and its frequency,
next we select each number and check whether it and other numbers can make
a sequence with size == k, if the pair exists, its frequency - 1 and if its 
frequency == 0, delete the number, we repeat this process until we meet a 
number needs the be pair but doesn't show up in remains numbers, then return
False, because the consecutive condition is violated 
"""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        nums.sort()
        d = dict()
        for num in nums:
            d[num] = d.get(num,0) + 1
        
        for num in nums:
            if num in d:
                for pair in range(num,num + k):
                    if pair in d:
                        d[pair] -= 1
                        if d[pair] == 0:
                            del d[pair]
                    else:
                        return False
        return True