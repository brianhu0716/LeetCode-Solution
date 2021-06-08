# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:48:24 2021

@author: Brian
"""
# import 
words = ["i", "love", "leetcode", "i", "love", "coding"]
k =3
d = {}
for word in words:
    if word not in d.keys():
        d[word] = 1
    else:
        d[word] += 1
table,ans = sorted([[d[key],key] for key in d.keys()])[::-1],[]
l = len(table)
while k > 0:
    if (l > 1 and table[0][0] != table[1][0]) or l == 1:
        ans += [table.pop(0)[1]]
        k -= 1
        l -= 1
    else:
        for i in range(l + 1):
            if i == l:
                i = l
                break
            elif table[i][0] != table[0][0]:
                break
            else:
                continue
        table[:i] = table[:i][::-1]
        print(table)
        c = 0
        while k > 0 and c < i:
            ans += [table.pop(0)[1]]
            k -= 1
            c += 1
            l -= 1
            print(ans)
print(ans)
