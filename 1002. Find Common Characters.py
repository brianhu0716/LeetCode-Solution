# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:48:13 2021

@author: -
"""
'''
思路與350雷同
值得注意的是海象運算符號的應用(#21)
'''
A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
ls = len(A)
d = {i:{} for i in range(ls)}
for i in range(ls):
    for l in A[i]:
        if l not in d[i].keys():
            d[i][l] = 1
        else:
            d[i][l] += 1

ir = (l := [len(d[i]) for i in range(ls)]).index(min(l))
result = []
for k in d[ir].keys():
    nk = []
    for i in range(ls):
        if k not in d[i].keys():
            break
        else:
            nk += [d[i][k]]
    if len(nk) == ls:
        result += [k] * min(nk)
print(result)
