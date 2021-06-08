# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:15:23 2021

@author: Brian
"""

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ref = [i for i in range(1,n + 1)]
        
        if k == 1 : return ref
        
        if k == 2 : return [ref.pop()] + ref
        
        ans,n_diff = [ref.pop(0)],0
        
        while k - n_diff > 1:
            if k - n_diff == 2 and len(ref) > 2 :
                return ans + [ref.pop()] + ref[::-1]
                
            ans += [ref.pop(),ref.pop(0)]
            n_diff += 2
        
        if n_diff == k: return ans
        
        return ans + ref