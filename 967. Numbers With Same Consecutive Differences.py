# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 00:54:17 2021

@author: Brian
"""
"""
because the leading zero is invalid, we control the prefix number from [1,10]. Then doing dfs to search answer
(a) for any "last digit", if we can add it or substract it by k so that the result in the range [0,10], it can be a part of valid answer. So we add the result to the string and add total digits by one, then continue dfs processing
(b) if the total digits equals to n, it means we find a valid answer
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(s,digit):
            if digit == n: # base case
                self.ans.add(int(s))
                return 
            
            num = int(s[-1]) # last digit in current number
            if num - k >= 0: # the next digit could be num - k
                dfs(s + str(num - k), digit + 1)
            if num + k < 10: # the next digit could be num + k
                dfs(s + str(num + k), digit + 1)
    
        self.ans = set()
        for prefix in range(1,10): # avoid leading zero
            dfs(str(prefix),1)
        
        return self.ans