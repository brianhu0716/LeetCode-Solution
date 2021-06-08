# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:01:01 2021

@author: Brian
"""
'''
與451,692,973,1366題類似
'''
nums = [1,1,1,2,2,2,3]
d = {}
for n in nums:
    if n not in d.keys():
        d[n] = 1  
    else :
        d[n] += 1
table = sorted([[d[key],key] for key in d.keys()])
ans = []
while (l := len(table)) > 0 :
    if (l > 1 and table[0][0] != table[1][0]) or l == 1:
        n = table.pop(0) 
        ans += [n[1]] * n[0] 
    else:
        for i in range(l + 1):
            if i == l:
                i = l
            elif table[i][0] != table[0][0]:
                break
            else:
                continue
        table[:i] = table[:i][::-1]
        for j in range(i):
            n = table.pop(0) 
            ans += [n[1]] * n[0]
print(ans)
        
        
            
# ans = [freq[1] for freq in table]
