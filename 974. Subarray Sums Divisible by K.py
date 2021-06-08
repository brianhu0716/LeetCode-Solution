# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:16:25 2021

@author: brian.hu
"""
"""
目標：(prefix_sum[:i] - prefix_sum[:j]) % k == 0 for i > j
等效於(prefix_sum[:i] & k) == (prefix_sum[:j] % k)
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = 0
        ans = 0
        d = collections.defaultdict(int)
        d[0] = 1
        for i in range(len(A)) :
            prefix_sum += A[i]
            ans += d[prefix_sum % K]
            d[prefix_sum % K] += 1
        return ans