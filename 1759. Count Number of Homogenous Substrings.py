# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:58:44 2021

@author: Brian
"""
'''
"aaaa"共有"a":4個、"aa":3個、"aaa":2個、"aaaa"；1個，所以一串子字串的總長度可以寫成(1 + lsub_s) * lsub_s / 2，由此我們
止需要再該字串中找到同一個字組成的子字串後，依上述公式計算各類型的子字串出現的次數，最後回傳總次數即可
'''
class Solution:
    def findLastWord(self,s,start,end,flag):
        for i in range(start, end):
            if s[i] != flag:
                return i
        return end
    def countHomogenous(self, s: str) -> int:
        ls,i,ans = len(s),0,0
        while i < ls:
            finish = self.findLastWord(s,i + 1,ls,s[i])
            ans += (1 + finish - i) * (finish - i) // 2
            i = finish
        return ans % 1000000007 if ans >= 1000000007 else ans
        '''
        ls,i,d = len(s),0,{}
        while i < ls:
            ref = s[i]
            sub_s = ref
            d[sub_s] = d.get(sub_s,0) + 1
            for j in range(i + 1,ls + 1):
                if j == ls:
                    i = ls
                    break
                if s[j] == ref:
                    sub_s += s[j]
                    for k in range(len(sub_s)):
                        d[ref * k] = d.get(ref * k,0) + 1
                else:
                    i = j
                    break
        return sum(list(d.values()))
        '''