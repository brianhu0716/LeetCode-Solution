# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:09:01 2021

@author: Brian Hu
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        tot, notsat = 0, 0 # number of total customers, number of unsatisfied customers
        prefix_sum = [0] # accumulate number of unsatisfied customers so far
        for i in range(len(customers)):
            tot += customers[i]
            if grumpy[i] == 1:
                notsat += customers[i]
                prefix_sum.append(prefix_sum[-1] + customers[i])
            else:
                prefix_sum.append(prefix_sum[-1])
        
        tolerate = 0 # optimize "tolerate" to let the number of unsatisfied customers in range [i : i + X] is maximized 
        for i in range(len(customers)):
            if (grumpy[i] == 0) or (grumpy[i] == 1 and customers[i] == 0):
                continue
            tolerate = max(tolerate, prefix_sum[min(i + X, len(prefix_sum) - 1)] - prefix_sum[i])
        return tot - (notsat - tolerate) 