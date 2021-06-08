# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:37:51 2021

@author: brian.hu
"""
"""
下一輪的答案是這一輪數字中各連續相同的數字的 個數 + 值 組合而成
ex :
    11 -- > 21(前一輪是一個1組成) --> 1211(前一輪是一個2組成 + 一個1 組成)
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        cnt = 2
        ans = "1"
        while cnt <= n :
            res = ""
            start = 0
            for i in range(1,len(ans) + 1):
                if i == len(ans) :
                    res += str((len(ans) - start)) + ans[i - 1] 
                    break
                if ans[i] != ans[i - 1] :
                    res += str((i - start)) + ans[i - 1]
                    start = i
            ans = res[:]
            cnt += 1
        return ans