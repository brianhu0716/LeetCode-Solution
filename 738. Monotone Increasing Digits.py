# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:02:20 2021

@author: Brian Hu
"""

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        sn = str(n)
        for i in range(len(sn) - 1):
            if sn[i] > sn[i + 1]: # violate monotonic increasing
                flag = str(int(sn[i]) - 1)
                for j in range(i,-2,-1):
                    if j == -1 or sn[j] <= flag:
                        return int(sn[:j + 1] + flag + "9" * (len(sn) - (j + 2)))
        return n
testcase = [10,
            1234,
            332,
            133453,
            1243,
            1241,
            ]
'''ans
9
1234
299
133449
1239
1239
'''